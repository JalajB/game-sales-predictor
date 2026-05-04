import numpy as np
import pandas as pd

# Load data
df = pd.read_csv("vgsales_features.csv")

# Separate features and target
X = df.drop(columns=["Global_Sales"]).values.astype(np.float64)  # shape: (16291, 620)
y = np.log1p(df["Global_Sales"].values.astype(np.float64))                  # shape: (16291,)

# Normalize X (important - keeps gradient descent stable)
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_std[X_std == 0] = 1  # avoid division by zero
X = (X - X_mean) / X_std

# Normalize y
y_mean = y.mean()
y_std = y.std()
y = (y - y_mean) / y_std

# Train/test split (80/20)
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Initialize weights and bias
np.random.seed(42)
w = np.zeros(X_train.shape[1])
b = 0.0

# Hyperparameters
lr = 0.01
epochs = 2000
n = len(X_train)

# Training loop
losses = []
for epoch in range(epochs):
    # Forward pass
    y_pred = X_train @ w + b

    # Loss (MSE)
    loss = np.mean((y_pred - y_train) ** 2)
    losses.append(loss)

    # Gradients
    dw = (2/n) * X_train.T @ (y_pred - y_train)
    db = (2/n) * np.sum(y_pred - y_train)

    # Update weights
    w = w - lr * dw
    b = b - lr * db

    if epoch % 50 == 0:
        print(f"Epoch {epoch} Loss: {loss:.4f}")



import matplotlib.pyplot as plt

plt.plot(losses)
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Training Loss Curve")
plt.savefig("loss_curve.png")
plt.show()

# Save everything
np.save("weights.npy", w)
np.save("bias.npy", np.array([b]))
np.save("X_mean.npy", X_mean)
np.save("X_std.npy", X_std)
np.save("y_mean.npy", np.array([y_mean]))
np.save("y_std.npy", np.array([y_std]))

print("Training done. Weights saved.")