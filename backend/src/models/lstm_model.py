from pathlib import Path

import joblib
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET = PROJECT_ROOT / "datasets" / "train_scaled.csv"
MODEL_PATH = PROJECT_ROOT / "saved_models" / "lstm.keras"
SCALER = PROJECT_ROOT / "saved_models" / "scaler.pkl"

WINDOW_SIZE = 20

FEATURE_COLUMNS = [
    "OrbitPhase (%)",
    "Sunlight (0 or 1)",
    "BusVoltage (V)",
    "BusCurrent (A)",
    "BatteryVoltage (V)",
    "BatteryTemperature (°C)",
    "BatterySOC (%)",
    "SolarVoltage (V)",
    "SolarCurrent (A)",
    "WheelRPM (RPM)",
    "WheelTemperature (°C)",
    "CPUUsage (%)",
    "CPUTemperature (°C)",
    "SignalStrength (dBm)",
    "GyroMagnitude (deg/s)",
    "Altitude (km)"
]

TARGET = "FaultLabel"


import pandas as pd

df = pd.read_csv(DATASET)

X = []
y = []

features = df[FEATURE_COLUMNS].values
labels = df[TARGET].values

for i in range(len(df) - WINDOW_SIZE):
    X.append(features[i:i+WINDOW_SIZE])
    y.append(labels[i+WINDOW_SIZE])

X = np.array(X)
y = np.array(y)

model = Sequential([
    LSTM(64, input_shape=(WINDOW_SIZE, len(FEATURE_COLUMNS))),
    Dropout(0.2),
    Dense(32, activation="relu"),
    Dense(7, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    X,
    y,
    epochs=10,
    batch_size=64,
    validation_split=0.2,
    verbose=1
)

model.save(MODEL_PATH)

print("\nModel Saved")