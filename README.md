# OCR_Chatbot_assignment

```markdown
# OCR Project PoC

This project demonstrates an OCR application using the QWEN VL-2 model from Hugging Face.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/OCR_Project.git
   cd OCR_Project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place images to process in the `input_images` directory.

2. Run the project:
   ```bash
   python main.py
   ```

3. Extracted text will be displayed in the console.

## Directory Structure

```
OCR_Project/
|-- main.py
|-- constants.py
|-- paths.py
|-- config.py
|-- requirements.txt
|-- README.md
|-- src/
    |-- __init__.py
    |-- ocr_engine.py
    |-- preprocessing.py
    |-- utils.py
```

## Features

- State-of-the-art OCR using QWEN VL-2.
- Object-oriented design.
- Clean code adhering to PEP8 standards.
- Easily extensible architecture.