import sys
import os
from PIL import Image  # Add this import
from src.ocr_engine import OCREngine
from src.preprocessing import convert_to_grayscale, denoise_image, resize_with_aspect_ratio
from config import Config
from paths import Paths

def main():
    # Specify the input image path
    image_path = os.path.join(Paths.INPUT_DIR, "sample_image.png")  # Update with your actual image file name

    # Check if the image exists before proceeding
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return  # Exit the function if the image isn't found

    # Step 1: Preprocess the image (can choose one or more preprocessing steps)
    print("Preprocessing image...")

    # Grayscale conversion
    preprocessed_image_path = convert_to_grayscale(image_path)
    print(f"Image after grayscale conversion saved at: {preprocessed_image_path}")
    
    # Denoising (optional, you can skip this if you don't want to use it)
    preprocessed_image_path = denoise_image(preprocessed_image_path)
    print(f"Image after denoising saved at: {preprocessed_image_path}")

    # Resize with aspect ratio (use a fixed size for consistency)
    preprocessed_image_path = resize_with_aspect_ratio(preprocessed_image_path, max_width=224, max_height=224)
    print(f"Image after resizing saved at: {preprocessed_image_path}")

    # Check image size
    with Image.open(preprocessed_image_path) as img:
        print(f"Preprocessed image size: {img.size}")  # This should be (224, 224) or close

    # Step 2: Initialize the OCR Engine with the model path
    ocr_engine = OCREngine(Config.OCR_MODEL_PATH)

    # Step 3: Perform OCR on the preprocessed image
    extracted_text = ocr_engine.perform_ocr(preprocessed_image_path)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("OCR failed to extract text.")

if __name__ == "__main__":
    main()
