from PIL import Image
import os

def preprocess_image(image_path, max_size):
    """
    Preprocess the image by resizing it to the specified maximum size.

    Args:
        image_path (str): Path to the input image.
        max_size (tuple): Maximum width and height for the image.

    Returns:
        str: Path to the preprocessed image.
    """
    with Image.open(image_path) as img:
        img.thumbnail(max_size)
        preprocessed_path = os.path.splitext(image_path)[0] + "_preprocessed.png"
        img.save(preprocessed_path, "PNG")
        return preprocessed_path