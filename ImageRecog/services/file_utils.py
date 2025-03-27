# core/services/file_utils.py
import os
from django.conf import settings
from uuid import uuid4

def handle_uploaded_file(uploaded_file):
    """Save uploaded file to media/temp with unique name"""
    temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    
    ext = os.path.splitext(uploaded_file.name)[1]
    filename = f"{uuid4().hex}{ext}"
    filepath = os.path.join(temp_dir, filename)
    
    with open(filepath, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    
    return filepath