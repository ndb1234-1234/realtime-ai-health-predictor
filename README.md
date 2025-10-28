# 🚦 Health Data Analyzer  
**AI-powered health insights from PDF reports using React, Flask, and Machine Learning**

---

## 📚 Table of Contents
- [📝 Overview](#-overview)
- [✨ Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🔎 How It Works](#-how-it-works)
- [🧩 Dataset & Model](#-dataset--model)
- [🖼 Screenshots](#-screenshots)
- [🤝 Contributing](#-contributing)
- [⚖️ License](#-license)
- [📬 Contact](#-contact)

---

## 📝 Overview
**Health Data Analyzer** is an AI-powered web application designed for smart, automatic health triage.  

It extracts key health parameters from PDF reports, predicts probable diseases, and recommends the most relevant medical specialists for treatment—all with a modern **React frontend**, **Flask/Python backend**, and **Machine Learning model**.

🔗 *Realtime health data collection* is enabled by sensors attached to the human body, which monitor vital signs throughout the day.  
📄 Each uploaded PDF contains averaged readings of these health parameters over a full day, ensuring reliable and representative health insights.  
📊 This approach bridges **wearable sensor technology** with **smart analytics**, enabling daily health trends to be automatically analyzed and triaged.

---

## ✨ Features
- 📥 Upload PDF health reports and analyze key parameters (SpO₂, Heart Rate, Sleep, Stress, Steps, Periodic Cycle)
- 🩺 Predict which type of doctor to consult (e.g., Cardiologist, Pulmonologist)
- 🚨 Flag potential diseases based on abnormal health parameters
- ⚡ Instant results with clear recommendations
- 🖥 Modern, user-friendly web interface

---

## 🛠 Tech Stack
| Component | Technology |
|------------|-------------|
| **Frontend** | React.js |
| **Backend** | Flask (Python) |
| **Model** | scikit-learn (Decision Tree) |
| **Database** | PostgreSQL |
| **PDF Parsing** | PyMuPDF |

---

## 📁 Project Structure
ece_project/
├── health-backend/
│ ├── app.py # Flask backend
│ ├── train_model.py # ML training script
│ ├── health_train.csv # Training dataset
│ ├── health_model.pkl # Trained ML model
│ └── ... # Other backend files
├── health-frontend/
│ ├── src/App.js # React frontend logic
│ ├── public/
│ └── ... # Other frontend files

yaml
Copy code

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.10+
- Node.js 16+
- npm
- PostgreSQL

---

### 🧩 Steps

#### 1️⃣ Clone the Repository
git clone https://github.com/ndb1234-1234/realtime-ai-health-predictor.git
cd health-data-analyzer

#### 2️⃣ Install Backend Dependencies
cd health-backend
py -m pip install -r requirements.txt
# Or manually:
py -m pip install flask flask_sqlalchemy flask_cors pandas scikit-learn pymupdf psycopg2

### 3️⃣ Train the Model
py train_model.py

### 4️⃣ Start The Backend
py app.py

### 5️⃣ Install Frontend Dependencies
cd ../health-frontend
npm install

### 6️⃣ Start The Frontend
npm start

### 7️⃣ Open in Browser

Visit http://localhost:3001
 (or the port React shows)

 🔎 How It Works

📄 Choose and upload a PDF with health data.

🤖 Backend extracts six key health features using PyMuPDF.

🧠 Machine Learning model predicts probable disease & doctor type.

🔗 Database stores reports for history/logging.

🖥 Frontend displays extracted data, predictions, and recommendations.

🧩 Dataset & Model
Training Data: health_train.csv (30 synthetic records, editable for retraining)
Model: Decision Tree (scikit-learn)
Targets:
⚕ Doctor (specialist to consult)
🦠 Disease (most likely issue based on parameters)

To retrain:
# Edit health_train.csv
py train_model.py

🖼 Screenshots
<img width="1907" height="963" alt="111" src="https://github.com/user-attachments/assets/08582146-0d8e-456e-8c83-3295ec828bb3" />
<img width="1912" height="958" alt="112" src="https://github.com/user-attachments/assets/794d2704-f52f-49ce-b0b0-6fc2a1047259" />
<img width="573" height="896" alt="113" src="https://github.com/user-attachments/assets/2ab8f846-b5c2-480d-87d1-a349176cea4f" />
<img width="1918" height="1017" alt="114" src="https://github.com/user-attachments/assets/08a12555-6a04-4999-93e2-a929a97fac69" />
<img width="1912" height="743" alt="115" src="https://github.com/user-attachments/assets/3850b2fa-19ee-405f-9168-6ac8fc0b1b2d" />
<img width="1918" height="1018" alt="116" src="https://github.com/user-attachments/assets/fc77eb05-4ab5-4cdf-badc-de5dbcd29add" />

🤝 Contributing

Contributions are welcome!
Please fork the repo and submit a pull request.
For major changes, open an issue first to discuss your ideas.

⚖️ License

This project is licensed under the MIT License.

📬 Contact

Created by: NEMALA DHANA BABU
📧 Email: 2300040368eceelge@gmail.com
