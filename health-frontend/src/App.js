import React, { useState } from 'react';
import './App.css';

const FIELDS = [
  { key: "SpO2", label: "SpO₂ (%)" },
  { key: "HeartRate", label: "Heart Rate (bpm)" },
  { key: "Sleep", label: "Sleep (hrs)" },
  { key: "Stress", label: "Stress" },
  { key: "Steps", label: "Steps" },
  { key: "PeriodicCycle", label: "Periodic Cycle" }
];

function App() {
  const [pdfFile, setPdfFile] = useState(null);
  const [healthData, setHealthData] = useState(null);
  const [doctor, setDoctor] = useState('');
  const [disease, setDisease] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setPdfFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!pdfFile) return alert("Please select a PDF file.");
    setLoading(true);

    const formData = new FormData();
    formData.append('pdf', pdfFile);

    const resp = await fetch('http://127.0.0.1:8000/upload', {
      method: 'POST',
      body: formData,
    });
    const json = await resp.json();
    setHealthData(json.data);
    setDoctor(json.predicted_doctor);
    setDisease(json.predicted_disease);
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="app-card">
        <h1 className="title">Health Data Analyser</h1>
        <div className="upload-section">
          <input type="file" accept="application/pdf" onChange={handleFileChange} className="file-input" id="file-upload" style={{ display: 'none' }} />
          <label htmlFor="file-upload" className="custom-file-label">
            {pdfFile ? pdfFile.name : "Choose PDF File"}
          </label>
          <button className="upload-btn" onClick={handleUpload} disabled={!pdfFile || loading}>
            {loading ? "Processing..." : "Upload & Analyze"}
          </button>
        </div>
        {healthData && (
          <div className="section">
            <h2 className="section-title">Parameters</h2>
            <div className="data-table">
              {FIELDS.map(({ key, label }) => (
                <div className="data-row" key={key}>
                  <span className="key">{label}</span>
                  <span className="value">
                    {healthData[key] !== undefined && healthData[key] !== null && healthData[key] !== ""
                      ? healthData[key]
                      : <span style={{ color: "#cc4040" }}>Not found</span>
                    }
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}
        {(doctor || disease) && (
          <div className="section">
            <h2 className="section-title">AI Recommendation</h2>
            {doctor && (
              <p>
                <strong>Doctor to consult:</strong> {doctor}
              </p>
            )}
            {disease && (
              <p>
                <strong>Predicted disease:</strong> {disease}
              </p>
            )}
          </div>
        )}
      </div>
      <footer className="footer">
        &copy; {new Date().getFullYear()} Health Insights
      </footer>
    </div>
  );
}

export default App;
