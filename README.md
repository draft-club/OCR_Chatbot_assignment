# OCR Chatbot Assignment

## Overview
This project is an Optical Character Recognition (OCR) chatbot that extracts text from images. Initially, the system was designed to use the **QWEN VL-2** model from Hugging Face, but modifications were required due to model availability and performance issues. The final implementation uses **Microsoft's TrOCR** model, which provided the best balance of accuracy and reliability.

## Modifications and Improvements

### Issues with the Initial Model (`qwen-vl-2`)
1. The model was unavailable on Hugging Face, returning a **404 error** when attempting to load it.
2. Other tested alternatives, including:
   - `microsoft/trocr-base-handwritten`
   - `microsoft/layoutlmv3-base`
   - `qwen-vl-2`
   
   These models either failed to extract meaningful text or returned random characters instead of actual words.

3. The best results were obtained with **`microsoft/trocr-large-printed`**, although it was not fully accurate in all cases.

### Enhancements Implemented
- **Preprocessing Adjustments**:  
  - Added grayscale conversion and binarization to improve text contrast.
  - Introduced noise reduction techniques using Non-Local Means Denoising.
  - Resized images to a standardized format for consistent OCR performance.

- **Streamlit Web Application**:  
  - Built a user-friendly interface for uploading images and displaying extracted text.
  - Integrated PDF processing functionality to handle multi-page documents.

- **Deployment and Authentication**:
  - Configured the application for deployment on Streamlit Cloud.
  - Used GitHub authentication via Personal Access Token (PAT) for secure repository access.



## Directory Structure
```
OCR_Chatbot_assignment/
|-- app.py
|-- config.py
|-- constants.py
|-- main.py
|-- README.md
|
|-- input_images/             # Directory for storing input images for OCR
|
|-- output/                   # Directory for storing processed images/text output
|
|-- pdf_pages/                # Directory for storing extracted pages from PDFs
|   |-- page_1.png            # Example extracted page from a PDF
|
|-- src/                      # Source code directory
|   |-- ocr_engine.py          # Main OCR processing script
|   |-- preprocessing.py       # Preprocessing functions (grayscale, binarization, noise removal)
|   |-- utils.py               # Utility functions
|   |-- tempCodeRunnerFile.py  # Temporary file created by VS Code
|-- venv/                     # Virtual environment (dependencies)
```

## Future Improvements
- Fine-tune `microsoft/trocr-large-printed` on domain-specific datasets.
- Implement adaptive thresholding for better OCR accuracy.
- Integrate AI-based post-processing to correct OCR errors.
