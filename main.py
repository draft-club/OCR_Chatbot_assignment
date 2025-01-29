import os
from src.ocr_engine import OCREngine
from src.preprocessing import preprocess_pipeline
from config import Config
from paths import Paths

def main():
    print("Starting OCR pipeline...")

    # Use Sample-image.png directly instead of PDF conversion
    image_path = os.path.join(Paths.INPUT_DIR, "Sample-image.png")

    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return

    print(f"Using image: {image_path}")

    # Preprocessing
    preprocessed_image = preprocess_pipeline(image_path)
    if preprocessed_image is None:
        print("Preprocessing failed.")
        return

    print(f"Using preprocessed image: {preprocessed_image}")

    # Initialize OCR engine
    ocr_engine = OCREngine(Config.OCR_MODEL_PATH)

    print("Running OCR...")
    extracted_text = ocr_engine.perform_ocr(preprocessed_image)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("OCR failed to extract text.")

if __name__ == "__main__":
    main()

"""The initial model (qwen-vl-2) was unusable due to a 404 error on Hugging Face.
Alternative models,failed to extract meaningful text, often returning random characters instead of words.
The most reliable option was microsoft/trocr-large-printed, though it remains imperfect, especially 
with noisy images or uncommon fonts."""

"""
Ways to Improve OCR Performance:
   - Preprocessing Enhancements: Use adaptive thresholding, morphological operations, and deskewing to 
   improve text clarity.
   - Model Optimization: Fine-tune TrOCR on a specialized dataset and apply data augmentation.
"""
