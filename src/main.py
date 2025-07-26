from src.model.prediction import predict_construction_violation

if __name__ == "__main__":
    image_path = "data/sample_satellite_data/sample_image_1.tif"
    results = predict_construction_violation(image_path)
    print("Predicted Violations:")
    print(results)
