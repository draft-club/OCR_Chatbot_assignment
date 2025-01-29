import os
import streamlit as st
from src.ocr_engine import OCREngine
from src.preprocessing import convert_to_grayscale, denoise_image, resize_with_aspect_ratio
from src.utils import pdf_to_images
from config import Config

# Initialize OCR Engine
ocr_engine = OCREngine(Config.OCR_MODEL_PATH)

# Streamlit UI
st.title("OCR Application")
st.write("Upload an image or PDF to extract text.")

# File upload
uploaded_file = st.file_uploader("Upload an Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    # Create temporary directory for uploads
    temp_dir = "temp_uploads"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Save the uploaded file temporarily
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Check if it's a PDF
    if file_path.endswith(".pdf"):
        st.write("Processing PDF...")
        output_dir = os.path.join(temp_dir, "pdf_pages")
        os.makedirs(output_dir, exist_ok=True)

        # Convert PDF to images
        image_paths = pdf_to_images(file_path, output_dir)
        if not image_paths:
            st.error("Failed to process the PDF.")
        else:
            st.write(f"PDF successfully converted into {len(image_paths)} pages.")
            selected_page = st.selectbox("Select a page for OCR", image_paths)
            file_path = selected_page  # Use the selected page as the image for OCR

    # Preprocessing Options
    st.write("Preprocessing Options")
    apply_grayscale = st.checkbox("Convert to Grayscale", value=True)
    apply_denoise = st.checkbox("Denoise Image", value=True)
    apply_resize = st.checkbox("Resize Image (448x448)", value=True)

    # Apply Preprocessing
    if file_path.endswith((".png", ".jpg", ".jpeg")):
        if apply_grayscale:
            file_path = convert_to_grayscale(file_path)
        if apply_denoise:
            file_path = denoise_image(file_path)
        if apply_resize:
            file_path = resize_with_aspect_ratio(file_path, target_size=(448, 448))

    # Perform OCR
    st.write("Performing OCR...")
    extracted_text = ocr_engine.perform_ocr(file_path)

    # Display Results
    if extracted_text:
        st.subheader("Extracted Text")
        st.text_area("Result", extracted_text, height=300)
    else:
        st.error("OCR failed to extract text.")

# Clean up temporary files (optional)
if st.button("Clear Temporary Files"):
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    st.success("Temporary files cleared.")
