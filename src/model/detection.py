import cv2
from ultralytics import YOLO

model = YOLO('yolov5s.pt')

def detect_change(before_path, after_path):
    before = cv2.imread(before_path)
    after = cv2.imread(after_path)
    diff = cv2.absdiff(before, after)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
    return mask

def run_yolo(image_path):
    results = model(image_path)
    return results
