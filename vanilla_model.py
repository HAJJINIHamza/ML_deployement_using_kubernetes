# Build a simple model, what important is deployment.

import pickle

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegressionCV

data = load_iris()
X, y = data.data, data.target

print("X.shape :", X.shape, "y.shape:", y.shape)

model = LogisticRegressionCV(max_iter=200)
model.fit(X, y)

print("Model trained successfully")

with open("models/vanilla_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully.")
