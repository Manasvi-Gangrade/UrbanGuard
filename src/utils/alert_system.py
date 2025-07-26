def send_alert_violation(location, confidence):
    return {
        "location": location,
        "confidence": confidence,
        "status": "ALERT GENERATED"
    }
