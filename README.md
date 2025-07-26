
# UrbanGuard – Smart Monitoring System for Illegal Construction

UrbanGuard is an AI-powered geospatial surveillance platform designed to monitor, detect, and prevent illegal construction in growing urban regions using satellite imagery, drone data, GIS mapping, and citizen engagement.

## Problem Statement

Cities like Indore are facing a rapid rise in unauthorized construction. Traditional manual inspections are slow, inefficient, and unable to scale.

## Our Solution

UrbanGuard is a real-time monitoring platform that combines:

- Satellite, GIS, and drone-based imagery
- AI/ML-based change detection (YOLOv5 + OpenCV)
- Real-time alerts for authorities
- Citizen portal for reporting
- Authority dashboard with visual analytics

## Tech Stack

| Component      | Tools                                 |
|----------------|----------------------------------------|
| Frontend       | HTML, CSS, JS                          |
| Backend        | Python (Flask)                         |
| AI/ML          | YOLOv5, TensorFlow, OpenCV             |
| Mapping/GIS    | QGIS, MapboxGL, Leaflet, Folium        |
| Database       | PostgreSQL + PostGIS                   |
| Cloud          | AWS / GCP (storage, hosting)           |

## Folder Structure

urbanguard/
├── backend/               # Flask APIs and dashboard
├── frontend/              # Citizen portal (HTML/CSS/JS)
├── notebooks/             # AI pipeline demos
├── src/                   # Core detection and utils
├── data/                  # Sample image data
├── docs/                  # Documentation and diagrams

## Sample Demo Use-Case

```bash
python src/main.py
```

Outputs prediction from YOLOv5 on a sample satellite image.

## Citizen Portal Features

- Upload image of suspected construction
- Pinpoint location on map
- Track report status

## Admin Dashboard

- Live alerts with heatmaps
- Zone-wise statistics
- Violation resolution tracking

## Installation

```bash
git clone https://github.com/your-username/UrbanGuard.git
cd UrbanGuard
pip install -r requirements.txt
```

## License

MIT License © 2025 [Your Name]

## Team

Built for Indore Tech Hackathon 2025  
Developed by [Your Team Name]

---

# requirements.txt

# Core backend
Flask==2.3.2
gunicorn==21.2.0

# Image Processing
opencv-python==4.9.0.80
numpy==1.24.4

# AI/ML Models
ultralytics==8.0.173
tensorflow==2.13.0
scikit-learn==1.3.2
pandas==2.0.3

# Geospatial Mapping
mapboxgl==0.10.2
folium==0.15.1

# Database (optional)
psycopg2-binary==2.9.9

# Notebook Support
matplotlib==3.7.1
jupyterlab==4.0.8
