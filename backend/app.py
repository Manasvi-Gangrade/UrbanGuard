from flask import Flask, request, jsonify
from src.utils.alert_system import send_alert_violation

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    result = send_alert_violation(data['location'], data['confidence'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
