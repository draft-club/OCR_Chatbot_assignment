import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_dir):
    #Convert a PDF file into individual images.
    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found at {pdf_path}")
        return None

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        images = convert_from_path(pdf_path, dpi=300)
        image_paths = []
        for i, image in enumerate(images):
            image_path = os.path.join(output_dir, f"page_{i+1}.png")
            image.save(image_path, "PNG")
            image_paths.append(image_path)
            print(f"Saved: {image_path}")

        return image_paths
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return None
