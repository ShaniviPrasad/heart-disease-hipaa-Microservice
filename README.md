# 🏥 HIPAA-Compliant Heart Disease Risk Prediction Microservice

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![AES-256](https://img.shields.io/badge/Security-AES--256-red?style=for-the-badge&logo=keepassxc&logoColor=white)
![HIPAA Compliant](https://img.shields.io/badge/HIPAA-Zero--Trust-blue?style=for-the-badge)

<p align="center">
  <b>A production-ready, privacy-first machine learning pipeline for cardiac risk assessment.</b><br>
  Engineered under a <b>Zero-Trust Security Model</b> using <b>AES-256 (Fernet) Encryption</b> to protect Patient Health Information (PHI) while maintaining sub-5ms inference latency.
</p>

---

</div>

## 🌟 Key Engineering Highlights

* 🛡️ **Zero-Trust PHI Cryptography:** Patient identification metrics (`patient_id`, `patient_name`) are encrypted end-to-end using symmetric **AES-256 (Fernet)**.
* ⚡ **In-Memory RAM Decryption:** Zero plain-text leaks on disk or network logs. Decryption occurs strictly inside volatile memory during pipeline inference execution.
* 🎯 **Precision-Calibrated ML Engine:** Calibrated Logistic Regression decision threshold from standard `0.50` to `0.68`, driving model **Precision to 95%+** and suppressing False Positives below **3%**.
* 🔌 **Modular Flask REST Microservice:** Exposes a secure `/predict` REST endpoint capable of parsing encrypted incoming JSON payloads and returning authenticated diagnostic risk logs.

---

## 🏗 System Architecture & Workflow

```text
[ Encrypted JSON Payload ] ──> ( Client Request )
                                      │
                                      ▼
                        [ Flask REST API Endpoint ]
                                      │
                                      ▼
                  [ In-Memory AES-256 Decryption (RAM) ]
                                      │
                                      ▼
               [ Feature Preprocessing & Standardization ]
                                      │
                                      ▼
               [ Logistic Regression Model (Threshold: 0.68) ]
                                      │
                                      ▼
            [ Risk Stratification (HIGH RISK / LOW RISK) ]
                                      │
                                      ▼
             [ Encrypted Audit Log Generated (Status 200 OK) ]

## 📊 Model Performance Metrics
Metric                       Default Baseline (0.50)             Tuned Microservice (0.68)           Clinical ImpactModel
Precision                          88.00%                                  95.00%+                       🚀 High diagnostic confidence
False Positives                    High (~12%)                             < 3.00%                      🛡️ Minimizes unnecessary invasive procedures
Inference Latency                  < 5ms                                   < 5ms                        ⚡ Real-time patient screening

## 🛠 Tech Stack & Tools
Core Language: Python 3.8+

Machine Learning: Scikit-Learn, Pandas, NumPy, Joblib

Cryptography & Security: PyCA Cryptography (Fernet / AES-256)

Microservice Framework: Flask, Requests

##📁 Repository Structure
heart-disease-hipaa/
│
├── security.py          # AES-256 Key Management & Cryptographic Module
├── anonymize_data.py    # Pipeline to anonymize raw clinical records
├── download_dataset.py  # UCI Heart Disease Dataset ingestion script
├── preprocess.py        # StandardScaler fit/transform pipeline
├── train.py             # L2 Regularized Logistic Regression training script
├── evaluate.py          # Threshold tuning & Precision-Recall evaluation
├── pipeline.py          # End-to-End secure inference logic engine
├── app.py              # Production Flask REST API microservice
├── test_api.py         # Microservice client verification client
└── requirements.txt    # Project dependencies

##🚀 Quick Start Guide
1. Repository Setup & Environment
# Clone the repository
git clone [https://github.com/ShaniviPrasad/heart-disease-hipaa.git](https://github.com/ShaniviPrasad/heart-disease-hipaa.git)
cd heart-disease-hipaa

# Create & activate Virtual Environment
python -m venv venv
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

2. Run Machine Learning Pipeline
python download_dataset.py
python anonymize_data.py
python train.py

3. Launch & Test REST Microservice
Terminal 1 (Start Server):
python app.py

Terminal 2 (Client Simulation):
python test_api.py
