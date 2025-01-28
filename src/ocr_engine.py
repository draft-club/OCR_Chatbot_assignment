"""This module encapsulates the OCR logic using the QWEN VL-2 model."""


from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import numpy as np
from constants import Constants

class OCREngine:
    def __init__(self, model_path):
        self.processor = AutoProcessor.from_pretrained(model_path)
        self.model = AutoModelForVision2Seq.from_pretrained(model_path)

    def perform_ocr(self, image_path):
        image = Image.open(image_path)

        # Preprocess image
        inputs = self.processor(images=image, return_tensors="pt")

        # Perform inference
        outputs = self.model.generate(**inputs)
        text = self.processor.batch_decode(outputs, skip_special_tokens=True)[0]
        return text