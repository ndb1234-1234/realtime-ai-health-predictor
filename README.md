🚦 Health Data Analyzer
AI-powered health insights from PDF reports using React, Flask, and Machine Learning

📚 Table of Contents
📝 Overview

✨ Features

🛠 Tech Stack

📁 Project Structure

🚀 Getting Started

🔎 How It Works

🧩 Dataset & Model

🖼 Screenshots

🤝 Contributing

⚖️ License

📬 Contact

📝 Overview
Health Data Analyzer is an AI-powered web application designed for smart, automatic health triage.

It extracts key health parameters from PDF reports, predicts probable diseases, and recommends the most relevant medical specialists for treatment—all with a modern React frontend, Flask/Python backend, and machine learning model.

🔗 Realtime health data collection is enabled by sensors attached to the human body, which monitor vital signs throughout the day.
📄 Each PDF file uploaded to the system contains the averaged readings of these health parameters over a full day, ensuring more reliable, representative insights for patient health assessment.
📊 This approach bridges wearable sensor technology with smart analytics: allowing daily health trends from patient devices to be instantly analyzed, flagged, and triaged by the Data Analyzer.

✨ Features
📥 Upload PDF health reports and analyze key parameters (SpO₂, Heart Rate, Sleep, Stress, Steps, Periodic Cycle)

🩺 Predict which type of doctor to consult (e.g., Cardiologist, Pulmonologist)

🚨 Flag potential diseases based on abnormal health parameters

⚡ Results displayed instantly with clear recommendations

🖥 Modern, user-friendly web interface

🛠 Tech Stack
Frontend: React.js

Backend: Flask (Python)

Model: scikit-learn (Decision Tree)

Database: PostgreSQL (for report storage)

PDF Parsing: PyMuPDF

📁 Project Structure
text
ece_project/
├── health-backend/
│   ├── app.py                 # Flask backend
│   ├── train_model.py         # ML training script
│   ├── health_train.csv       # Training dataset
│   ├── health_model.pkl       # Trained ML model
│   └── ...                    # Other backend files
├── health-frontend/
│   ├── src/App.js             # React frontend logic
│   ├── public/
│   └── ...                    # Other frontend files
🚀 Getting Started
Prerequisites
Python 3.10+

Node.js 16+

npm

PostgreSQL

Steps
Clone the Repository

bash
git clone https://github.com/yourusername/health-data-analyzer.git
cd health-data-analyzer
Install Backend Dependencies

bash
cd health-backend
py -m pip install -r requirements.txt
# Or manually:
py -m pip install flask flask_sqlalchemy flask_cors pandas scikit-learn pymupdf psycopg2
Train the Model

bash
py train_model.py
Start The Backend

bash
py app.py
Install Frontend Dependencies

bash
cd ../health-frontend
npm install
Start The Frontend

bash
npm start
Open in Browser

Visit http://localhost:3001 (or the port React shows).

🔎 How It Works
📄 Choose and upload a PDF with health data.

🤖 Backend extracts six health features using PyMuPDF.

🧠 ML model predicts probable disease & specialist on-the-fly.

🔗 Database stores uploaded reports for history/logging.

🖥 Frontend displays extracted parameters, model prediction, and doctor recommendation.

🧩 Dataset & Model
Training Data: health_train.csv (30 synthetic records, editable for retraining)

Model: Decision Tree (scikit-learn), trained on key parameters.

Targets:

⚕ Doctor (which specialist to consult)

🦠 Disease (most likely problem if any abnormality is found)

If you want to re-train, edit health_train.csv and re-run train_model.py.

🖼 Screenshots
<img width="1907" height="963" alt="111" src="https://github.com/user-attachments/assets/08582146-0d8e-456e-8c83-3295ec828bb3" /> <img width="1912" height="958" alt="112" src="https://github.com/user-attachments/assets/794d2704-f52f-49ce-b0b0-6fc2a1047259" /> <img width="573" height="896" alt="113" src="https://github.com/user-attachments/assets/2ab8f846-b5c2-480d-87d1-a349176cea4f" /> <img width="1918" height="1017" alt="114" src="https://github.com/user-attachments/assets/08a12555-6a04-4999-93e2-a929a97fac69" /> <img width="1912" height="743" alt="115" src="https://github.com/user-attachments/assets/3850b2fa-19ee-405f-9168-6ac8fc0b1b2d" /> <img width="1918" height="1018" alt="116" src="https://github.com/user-attachments/assets/fc77eb05-4ab5-4cdf-badc-de5dbcd29add" />
🤝 Contributing
Contributions welcome!
Please fork the repo and submit a pull request. For major changes, open an issue first to discuss.

⚖️ License
This project is licensed under the MIT License.

📬 Contact
Created by NEMALA DHANA BABU – 2300040368eceelge@gmail.com
