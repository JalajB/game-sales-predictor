import numpy as np
import pandas as pd

# Load saved weights and normalization values
w = np.load("weights.npy")
b = np.load("bias.npy")[0]
X_mean = np.load("X_mean.npy")
X_std = np.load("X_std.npy")
y_mean = np.load("y_mean.npy")[0]
y_std = np.load("y_std.npy")[0]

# Load feature column names so we know the exact order
feature_columns = pd.read_csv("vgsales_features.csv").drop(columns=["Global_Sales"]).columns.tolist()

def predict(platform: str, genre: str, year: int) -> float:
    # Build a zero row with all feature columns
    input_df = pd.DataFrame([{col: 0 for col in feature_columns}])

    # Set the relevant one-hot columns to 1
    if f"Platform_{platform}" in input_df.columns:
        input_df[f"Platform_{platform}"] = 1

    if f"Genre_{genre}" in input_df.columns:
        input_df[f"Genre_{genre}"] = 1

    input_df["Year"] = year

    # Convert to numpy and normalize
    x = input_df.values.astype(np.float64)
    x = (x - X_mean) / X_std

    # Forward pass
    y_pred_normalized = x @ w + b

    # Denormalize and reverse log transform
    y_pred = np.expm1(y_pred_normalized * y_std + y_mean)

    return round(float(y_pred.flatten()[0]), 4)