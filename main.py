### main.py
"""This is the entry point of the application."""

import os
from src.ocr_engine import OCREngine
from src.preprocessing import preprocess_image
from config import Config
from paths import Paths

def main():
    # Initialize OCR Engine
    ocr_engine = OCREngine(Config.OCR_MODEL_PATH)

    # Specify the input image path
    image_path = os.path.join(Paths.INPUT_DIR, "sample_image.png")

    # Preprocess the image
    preprocessed_image_path = preprocess_image(image_path, Config.MAX_IMAGE_SIZE)

    # Perform OCR
    extracted_text = ocr_engine.perform_ocr(preprocessed_image_path)

    print("Extracted Text:")
    print(extracted_text)

if __name__ == "__main__":
    main()
