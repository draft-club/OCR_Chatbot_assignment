import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import os

class OCREngine:
    def __init__(self, model_path="microsoft/trocr-large-printed"):
        """Initialize the OCR engine using TrOCR with a pretrained VisionEncoderDecoder model."""
        self.processor = TrOCRProcessor.from_pretrained(model_path)
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.model = VisionEncoderDecoderModel.from_pretrained(model_path).to(self.device)

        # Set up decoder configuration
        self.model.config.decoder_start_token_id = self.processor.tokenizer.eos_token_id
        self.model.config.pad_token_id = self.processor.tokenizer.pad_token_id
        self.model.config.vocab_size = self.model.config.decoder.vocab_size

    def preprocess_image(self, image_path, target_size=(1024, 1024)): 
        """Resize the image to the expected size for TrOCR."""
        try:
            if not os.path.exists(image_path):
                print(f"Error: Image not found at {image_path}")
                return None

            image = Image.open(image_path).convert("RGB")
            image = image.resize(target_size, Image.Resampling.LANCZOS)
            print(f"Resized image to: {target_size}")

            return image
        except Exception as e:
            print(f"Preprocessing error: {e}")
            return None

    def perform_ocr(self, image_path, preprocess=True):
        """Run OCR on an image and return extracted text."""
        try:
            if not os.path.exists(image_path):
                print(f"Error: Image not found at {image_path}")
                return None

            # Preprocess image
            image = self.preprocess_image(image_path) if preprocess else Image.open(image_path).convert("RGB")
            if image is None:
                return None

            inputs = self.processor(images=image, return_tensors="pt").to(self.device)
            print(f"Model input shape: {inputs['pixel_values'].shape}")

            print("Running OCR...")

            output_ids = self.model.generate(
            **inputs, 
            max_new_tokens=512,  # Increase from 256 to 512
            do_sample=False,  
            temperature=1.0,
            repetition_penalty=1.2,
            length_penalty=1.0,
            early_stopping=True,
            num_beams=5  # Beam search for better accuracy
)


            print("OCR completed, extracting text...")

            extracted_text = self.processor.batch_decode(output_ids, skip_special_tokens=True)
            print("Extracted text:", extracted_text)

            return extracted_text[0] if extracted_text else None
        except Exception as e:
            print(f"OCR error: {e}")
            return None
