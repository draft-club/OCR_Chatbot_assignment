from PIL import Image
import os

from PIL import Image
import os
from constants import Constants

def is_supported_format(file_name):
    return any(file_name.lower().endswith(ext) for ext in Constants.INPUT_IMAGE_FORMATS)