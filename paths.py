import os

class Paths:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR = os.path.join(BASE_DIR, "input_images")
    OUTPUT_DIR = os.path.join(BASE_DIR, "output")

    @staticmethod
    def ensure_dirs():
        os.makedirs(Paths.INPUT_DIR, exist_ok=True)
        os.makedirs(Paths.OUTPUT_DIR, exist_ok=True)

Paths.ensure_dirs()