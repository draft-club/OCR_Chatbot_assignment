import os
from PIL import Image
from src.ocr_engine import OCREngine
from src.utils import pdf_to_images
from config import Config
from paths import Paths

def main():
    print("Starting OCR pipeline...")

    pdf_path = os.path.join("input_images", "invoice_sample.pdf")
    output_dir = "pdf_pages"  # Directory where images will be saved

    image_paths = pdf_to_images(pdf_path, output_dir)  # Convert PDF to images

    if not image_paths or len(image_paths) == 0:
        print("Error: No images were generated from the PDF.")
        return

    image_path = image_paths[0]  # Select the first page

    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return

    print(f"Using image: {image_path}")

    # Ensure the image exists before opening
    with Image.open(image_path) as img:
        print(f"Final image size: {img.size}")
        img.show()

    print("Initializing OCR Engine...")
    ocr_engine = OCREngine(Config.OCR_MODEL_PATH)

    print("Running OCR...")
    extracted_text = ocr_engine.perform_ocr(image_path)

    if extracted_text:
        print("\nExtracted Text:\n", extracted_text)
    else:
        print("OCR failed to extract text.")

if __name__ == "__main__":
    main()
