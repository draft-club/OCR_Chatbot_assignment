import os
import cv2
import numpy as np
from PIL import Image

# Define output directory for processed images
OUTPUT_DIR = "output"

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_output_path(image_path, suffix):
    """Generate a new file path in the output directory with a suffix."""
    base_name = os.path.basename(image_path).replace(".png", f"_{suffix}.png")
    return os.path.join(OUTPUT_DIR, base_name)

def convert_to_grayscale(image_path):
    """Convert an image to grayscale and apply binarization for better OCR accuracy."""
    print(f"Converting to grayscale: {image_path}")
    
    # Load image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image {image_path}")
        return None

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Grayscale conversion done. Applying binarization...")

    # Apply Otsu's thresholding for binarization (helps with OCR contrast)
    _, binary_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the processed grayscale image
    preprocessed_path = get_output_path(image_path, "grayscale")
    cv2.imwrite(preprocessed_path, binary_img)
    print(f"Saved grayscale image to: {preprocessed_path}")
    
    return preprocessed_path

def denoise_image(image_path):
    """Apply noise reduction using Non-Local Means Denoising."""
    print(f"Denoising image: {image_path}")
    
    # Load the grayscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load image {image_path}")
        return None

    # Apply Non-Local Means Denoising
    denoised_img = cv2.fastNlMeansDenoising(img, None, h=30, templateWindowSize=7, searchWindowSize=21)

    # Save the denoised image
    preprocessed_path = get_output_path(image_path, "denoised")
    cv2.imwrite(preprocessed_path, denoised_img)
    print(f"Saved denoised image to: {preprocessed_path}")
    
    return preprocessed_path

def resize_with_aspect_ratio(image_path, target_size=(384, 384)):
    """Resize an image to a fixed size using high-quality interpolation."""
    print(f"Resizing image: {image_path}")
    
    # Load image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image {image_path}")
        return None

    # Resize the image while maintaining aspect ratio
    img_resized = cv2.resize(img, target_size, interpolation=cv2.INTER_LANCZOS4)
    
    # Save the resized image
    preprocessed_path = get_output_path(image_path, "resized")
    cv2.imwrite(preprocessed_path, img_resized)

    print(f"Saved resized image to: {preprocessed_path}")
    return preprocessed_path

def preprocess_pipeline(image_path):
    """Full preprocessing pipeline that applies grayscale conversion, denoising, and resizing."""
    print(f"Starting preprocessing for {image_path}")

    # Step 1: Convert image to grayscale and apply binarization
    grayscale_path = convert_to_grayscale(image_path)
    if grayscale_path is None:
        print("Error during grayscale conversion.")
        return None

    # Step 2: Apply denoising to reduce noise
    denoised_path = denoise_image(grayscale_path)
    if denoised_path is None:
        print("Error during denoising.")
        return None

    # Step 3: Resize the denoised image
    resized_path = resize_with_aspect_ratio(denoised_path)
    if resized_path is None:
        print("Error during resizing.")
        return None

    print(f"Preprocessing complete. Final image: {resized_path}")
    return resized_path

"""
The initial OCR model struggled to extract text accurately, requiring significant changes to preprocessing. 
The new approach includes grayscale conversion, denoising, binarization, and fixed-size resizing to enhance text
visibility. The original model (qwen-vl-2) failed, leading to a switch to microsoft/trocr-large-printed, 
which performed better. These adjustments ensure more reliable OCR results.
"""
