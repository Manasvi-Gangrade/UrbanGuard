from .detection import run_yolo

def predict_construction_violation(image_path):
    results = run_yolo(image_path)
    return results.pandas().xyxy[0]  # DataFrame with detections
