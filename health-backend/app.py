from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import fitz  # PyMuPDF for PDF parsing
import os
import pickle

app = Flask(__name__)
# Allow CORS for your frontend port
CORS(app, resources={r"/*": {"origins": "http://localhost:3001"}})

# PostgreSQL connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:9390@localhost/project_ece'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Load the trained ML model at startup
with open('health_model.pkl', 'rb') as f:
    model = pickle.load(f)

class HealthData(db.Model):
    __tablename__ = 'health_data'
    id = db.Column(db.Integer, primary_key=True)
    SpO2 = db.Column(db.String(10))
    HeartRate = db.Column(db.String(10))
    Sleep = db.Column(db.String(10))
    Stress = db.Column(db.String(15))
    Steps = db.Column(db.String(15))
    PeriodicCycle = db.Column(db.String(30))
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())

def extract_data_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    lines = text.splitlines()
    params = ["SpO2", "HeartRate", "Sleep", "Stress", "Steps", "Periodic Cycle"]
    result = {param: "" for param in params}
    for line in lines:
        for param in params:
            if param.replace(" ", "") in line.replace(" ", ""):
                parts = line.split(":")
                if len(parts) > 1:
                    result[param] = parts[1].strip()
    return result

def predict_doctor_disease(data):
    features = model['features']
    input_encoded = []
    for col in features:
        val = data.get(col, '')
        enc = model['encoders'][col]
        val_enc = enc.transform([val]) if val in enc.classes_ else [0]
        input_encoded.append(val_enc[0])
    X = [input_encoded]
    doctor_pred = model['doctor_encoder'].inverse_transform(model['clf_doctor'].predict(X))[0]
    disease_pred = model['disease_encoder'].inverse_transform(model['clf_disease'].predict(X))[0]
    return doctor_pred, disease_pred

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    f = request.files['pdf']
    temp_dir = 'tmp'
    os.makedirs(temp_dir, exist_ok=True)
    filepath = os.path.join(temp_dir, f.filename)
    f.save(filepath)
    data = extract_data_from_pdf(filepath)
    dbrow = HealthData(
        SpO2=data.get("SpO2", ""),
        HeartRate=data.get("HeartRate", ""),
        Sleep=data.get("Sleep", ""),
        Stress=data.get("Stress", ""),
        Steps=data.get("Steps", ""),
        PeriodicCycle=data.get("Periodic Cycle", "")
    )
    db.session.add(dbrow)
    db.session.commit()
    doctor, disease = predict_doctor_disease(data)
    return jsonify({
        "data": data,
        "predicted_doctor": doctor,
        "predicted_disease": disease
    })

@app.route('/', methods=['GET'])
def home():
    return "Backend running!", 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)
