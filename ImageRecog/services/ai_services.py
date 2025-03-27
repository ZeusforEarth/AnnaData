# core/services/ai_services.py
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from gpt4all import GPT4All
from django.conf import settings

class PestAIService:
    _instance = None
    
    def __init__(self):
        # Load CNN model
        cnn_path = os.path.join(settings.BASE_DIR, 'ImageRecog/models/pest_disease_recognition.h5')
        self.cnn_model = tf.keras.models.load_model(cnn_path)
        
        # Load LLM
        llm_path = os.path.join(settings.BASE_DIR, 'ImageRecog/models/mistral-7b-instruct-v0.1.Q4_0.gguf')
        self.solution_llm = GPT4All(llm_path)
        
        # Class labels (must match your training)
        self.class_labels = [
            "Disease_Black Rot", "Disease_Common Rust", "Disease_Early Blight",
            "Disease_Leaf Mold", "Disease_Powdery Mildew", "Pest_Aphids",
            "Pest_Armyworms", "Pest_Corn Earworms", "Pest_Spider Mites", "Pest_Thrips"
        ]

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PestAIService()
        return cls._instance

    def preprocess_image(self, img_path):
        img = image.load_img(img_path, target_size=(150, 150))
        img_array = image.img_to_array(img) / 255.0
        return np.expand_dims(img_array, axis=0)

    def predict_pest(self, image_path):
        img_array = self.preprocess_image(image_path)
        prediction = self.cnn_model.predict(img_array)
        class_idx = np.argmax(prediction)
        return {
            'class': self.class_labels[class_idx],
            'confidence': float(np.max(prediction)),
            'is_pest': self.class_labels[class_idx].startswith('Pest_')
        }

    def generate_solution(self, pest_name):
        prompt = f"""As an agricultural expert, provide detailed guidance for {pest_name} covering:
        1. Identification (Key visual symptoms)
        2. Biological Control (Organic solutions)
        3. Chemical Control (Recommended products)
        4. Prevention Measures
        Use bullet points and simple language."""
        return self.solution_llm.generate(prompt, max_tokens=400)

    def full_analysis(self, image_path):
        detection = self.predict_pest(image_path)
        solution = self.generate_solution(detection['class'])
        return {**detection, 'solution': solution}