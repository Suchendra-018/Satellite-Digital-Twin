from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    LSTM,
    Dense,
    Dropout,
    BatchNormalization,
)
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ReduceLROnPlateau,
)
from tensorflow.keras.optimizers import Adam


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET = PROJECT_ROOT / "datasets" / "train_scaled.csv"

MODEL_PATH = PROJECT_ROOT / "saved_models" / "lstm.keras"

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
    "Altitude (km)",
]

TARGET = "FaultLabel"


def build_sequences(features, labels):

    X = []
    y = []

    for i in range(len(features) - WINDOW_SIZE):
        X.append(features[i:i + WINDOW_SIZE])
        y.append(labels[i + WINDOW_SIZE])

    return np.array(X), np.array(y)


def build_model():

    model = Sequential([
        LSTM(
            128,
            return_sequences=True,
            input_shape=(
                WINDOW_SIZE,
                len(FEATURE_COLUMNS),
            ),
        ),

        Dropout(0.30),

        LSTM(64),

        BatchNormalization(),

        Dense(
            64,
            activation="relu",
        ),

        Dropout(0.30),

        Dense(
            32,
            activation="relu",
        ),

        Dense(
            7,
            activation="softmax",
        ),
    ])

    model.compile(
        optimizer=Adam(
            learning_rate=0.001,
        ),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    return model


def main():

    print("\nLoading Dataset...\n")

    df = pd.read_csv(DATASET)

    features = df[FEATURE_COLUMNS].values
    labels = df[TARGET].values

    X, y = build_sequences(
        features,
        labels,
    )

    print(f"Training Samples : {len(X)}")

    model = build_model()

    callbacks = [

        EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True,
        ),

        ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.5,
            patience=2,
            verbose=1,
        ),

    ]

    model.fit(
        X,
        y,
        epochs=30,
        batch_size=64,
        validation_split=0.20,
        callbacks=callbacks,
        verbose=1,
    )

    model.save(MODEL_PATH)

    print("\nLSTM Model Saved Successfully")


if __name__ == "__main__":
    main()