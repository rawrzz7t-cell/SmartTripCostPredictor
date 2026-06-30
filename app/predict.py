import joblib
import numpy as np
import tensorflow as tf
from pathlib import Path

# Folder project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load model
model = tf.keras.models.load_model(BASE_DIR / "models" / "ann_model.keras")

# Load scaler
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")


def predict_price(data):

    data = np.array(data).reshape(1, -1)

    data = scaler.transform(data)

    prediction = model.predict(data, verbose=0)

    return float(prediction[0][0])