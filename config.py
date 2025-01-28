### config.py
"""Store configuration settings."""


class Config:
    OCR_MODEL_PATH = "qwen-vl-2"  # Hugging Face model identifier
    MAX_IMAGE_SIZE = (1024, 1024)  # Resize image if larger
