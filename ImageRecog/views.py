import os
import gzip
import tempfile
import io
import numpy as np
import tensorflow as tf
from django.shortcuts import render, redirect
from django.conf import settings
from .models import PestDiseaseAnalysis
from .forms import ImageUploadForm
from tensorflow.keras.preprocessing import image
from gpt4all import GPT4All

# GPU Configuration
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_memory_growth(gpus[0], True)
        print("GPU memory growth enabled.")
    except RuntimeError as e:
        print(f"Error enabling GPU memory growth: {e}")
else:
    print("No GPU found. Running on CPU.")

# Global variables
COMPRESSED_MODEL_PATH = os.path.join(settings.BASE_DIR, 'ImageRecog', 'models', 'disease_recognition.h5.gz')

def load_compressed_model():
    """Safely load model from compressed .h5.gz file"""
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix='.h5', delete=False) as tmp_file:
            # Decompress directly to temp file
            with gzip.open(COMPRESSED_MODEL_PATH, 'rb') as f_in:
                tmp_file.write(f_in.read())
            temp_path = tmp_file.name
        
        # Load model from temp file
        model = tf.keras.models.load_model(temp_path)
        
        # Clean up temp file
        try:
            os.unlink(temp_path)
        except:
            pass
            
        print("Model successfully loaded from compressed file")
        return model
        
    except Exception as e:
        print(f"Failed to load model: {str(e)}")
        raise

# Initialize models
MODEL = load_compressed_model()
SOLUTION_MODEL = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf", device='cpu')  # Force CPU for GPT4All

# Class Labels
CLASS_LABELS = [
    "Disease_Black Rot", "Disease_Common Rust", "Disease_Early Blight", 
    "Disease_Leaf Mold", "Disease_Powdery Mildew", "Pest_Aphids", 
    "Pest_Armyworms", "Pest_Corn Earworms", "Pest_Spider Mites", "Pest_Thrips"
]

def preprocess_image(img_path):
    """Preprocess uploaded image for prediction"""
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def get_solution(pest_or_disease):
    """Generate treatment solution using GPT4All"""
    prompt = f"""
    As an agricultural expert, provide detailed guidance for: {pest_or_disease}
    Cover:
    1. Identification symptoms
    2. Organic treatment options
    3. Chemical treatments (with safety precautions)
    4. Prevention strategies
    5. Scientific references
    """
    return SOLUTION_MODEL.generate(prompt, max_tokens=300)

def index(request):
    """Main view handling image upload and prediction"""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save()
            try:
                # Prediction pipeline
                img_array = preprocess_image(analysis.image.path)
                prediction = MODEL.predict(img_array)
                predicted_class = CLASS_LABELS[np.argmax(prediction)]
                confidence = round(float(np.max(prediction)) * 100, 2)
                
                # Prepare results
                context = {
                    'uploaded_image_url': analysis.image.url,
                    'prediction': predicted_class.split('_')[1],
                    'is_pest': predicted_class.startswith('Pest_'),
                    'confidence': confidence,
                    'solution': get_solution(predicted_class)
                }
                return render(request, 'ImageRecog/imageout.html', context)
            
            except Exception as e:
                return render(request, 'ImageRecog/imagereco.html', {
                    'form': form,
                    'error': f"Prediction failed: {str(e)}"
                })
    
    form = ImageUploadForm()
    return render(request, 'ImageRecog/imagereco.html', {'form': form})