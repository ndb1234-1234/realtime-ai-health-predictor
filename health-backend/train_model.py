import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the training data
df = pd.read_csv('health_train.csv')

features = ['SpO2', 'HeartRate', 'Sleep', 'Stress', 'Steps', 'PeriodicCycle']
X = df[features]
y_doctor = df['Doctor']
y_disease = df['Disease']

encoders = {col: LabelEncoder().fit(X[col]) for col in features}
X_encoded = pd.DataFrame({col: encoders[col].transform(X[col]) for col in features})

doctor_encoder = LabelEncoder().fit(y_doctor)
y_doctor_encoded = doctor_encoder.transform(y_doctor)

disease_encoder = LabelEncoder().fit(y_disease)
y_disease_encoded = disease_encoder.transform(y_disease)

clf_doctor = DecisionTreeClassifier().fit(X_encoded, y_doctor_encoded)
clf_disease = DecisionTreeClassifier().fit(X_encoded, y_disease_encoded)

with open('health_model.pkl', 'wb') as f:
    pickle.dump({
        'clf_doctor': clf_doctor,
        'clf_disease': clf_disease,
        'encoders': encoders,
        'doctor_encoder': doctor_encoder,
        'disease_encoder': disease_encoder,
        'features': features
    }, f)

print("Model training complete. Model saved to health_model.pkl.")
