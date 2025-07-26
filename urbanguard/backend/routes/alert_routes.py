from flask import Blueprint, request, jsonify
from src.utils.alert_system import send_alert_violation

alert_routes = Blueprint('alert_routes', __name__)

@alert_routes.route('/api/alert', methods=['POST'])
def trigger_alert():
    data = request.json
    location = data.get("location", "Unknown")
    confidence = data.get("confidence", 0.0)
    result = send_alert_violation(location, confidence)
    return jsonify(result)
