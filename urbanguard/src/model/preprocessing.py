import cv2

def load_and_resize(image_path, size=(416, 416)):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    return cv2.resize(image, size)

def normalize_image(image):
    return image.astype('float32') / 255.0
