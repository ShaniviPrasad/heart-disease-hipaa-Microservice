
from flask import Flask, request, jsonify
from pipeline import SecureHeartDiseasePipeline
from security import encrypt_data, decrypt_data

app = Flask(__name__)
pipeline = SecureHeartDiseasePipeline()

@app.route('/health', methods=['GET'])
def health_check():
    """Server status check endpoint"""
    return jsonify({"status": "active", "service": "HIPAA-Compliant Heart Disease Risk API"})

@app.route('/predict', methods=['POST'])
def predict():
    """
    HIPAA Compliant Prediction Endpoint
    Expects JSON:
    {
        "encrypted_patient_id": "...",
        "encrypted_patient_name": "...",
        "clinical_features": [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    }
    """
    try:
        data = request.get_json()
        if not data or 'encrypted_patient_id' not in data or 'clinical_features' not in data:
            return jsonify({"error": "Invalid payload parameters"}), 400

        result = pipeline.predict_encrypted_patient(data)

        return jsonify({
            "status": "success",
            "patient_preview": result['decrypted_preview_for_doctor'],
            "encrypted_audit_log": result['encrypted_log_for_database']
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🌐 Starting HIPAA-Compliant Flask Server on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)