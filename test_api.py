import requests
from security import encrypt_data

API_URL = "http://127.0.0.1:5000/predict"

payload = {
    "encrypted_patient_id": encrypt_data("PAT_US_4091"),
    "encrypted_patient_name": encrypt_data("Anish Kapoor"),
    "clinical_features": [67, 1, 4, 160, 286, 0, 2, 108, 1, 1.5, 2, 3, 3]
}

print("📡 Sending Encrypted API Payload to Server...")
response = requests.post(API_URL, json=payload)

print(f"\n📥 Server Status Code: {response.status_code}")
print("📊 Response JSON:")
print(response.json())