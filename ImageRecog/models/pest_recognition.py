import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from gpt4all import GPT4All  # Change to transformers if using Hugging Face

# Load trained model
model = tf.keras.models.load_model("pest_disease_recognition.h5")

# Class Labels (Update based on dataset)
class_labels = [
    "Disease_Black Rot", "Disease_Common Rust", "Disease_Early Blight", 
    "Disease_Leaf Mold", "Disease_Powdery Mildew", "Pest_Aphids", 
    "Pest_Armyworms", "Pest_Corn Earworms", "Pest_Spider Mites", "Pest_Thrips"
]

# Load GPT4All Model (Offline)
solution_model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")


# Function to preprocess image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Function to get solution
def get_solution(pest_or_disease):
    prompt = f"""
    You are an expert agricultural consultant with vast knowledge of plant pests and diseases.
    Given the issue: {pest_or_disease}, provide a structured and detailed response covering:
    
    1️. **Identification:** Symptoms and how to confirm it.
    2️. **Biological Control:** Natural treatments and eco-friendly solutions.
    3. **Chemical Control:** Safe pesticides (mention active ingredients).
    4️. **Preventive Measures:** How to avoid recurrence.
    5️. **Scientific References:** Cite sources if available.

    Please format the response in clear bullet points.
    """
    
    response = solution_model.generate(prompt, max_tokens=300)
    return response

# Function to predict pest/disease and suggest a solution
def predict_and_suggest_solution(img_path):
    img_array = preprocess_image(img_path)
    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]
    
    print(f"Detected: {predicted_class}")
    solution = get_solution(predicted_class)
    
    print("\nSolution:")
    print(solution)


image_path = r"C:\Users\Ayesha\Downloads\archive (2)\farm_insects\Pest_Corn Earworms\Image_67.jpg"
predict_and_suggest_solution(image_path)
