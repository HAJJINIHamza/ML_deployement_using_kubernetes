# Build a simple model, what important is deployment.

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegressionCV
import pickle

data = load_iris()
X, y = data.data, data.target

model = LogisticRegressionCV(max_iter=200)
model.fit(X, y)

print ("Model trained successfully")

with open("moels/vanilla_model.pkl", "wb") as f:
    pickle.dump(model, f)

print ("Model saved successfully.")