import contextlib
import pickle
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from app.dependencies.get_model import get_model


class IrisVariables(BaseModel):
    s_length: float
    s_width: float
    p_length: float
    p_width: float


# Initiate model


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    try:
        with open("models/vanilla_model.pkl", "rb") as f:
            app.state.model = pickle.load(f)
    except FileNotFoundError:
        print("Can't find file")
        app.state.model = None
    except Exception as e:
        print(f"Error : {e}")
        app.state.model = None
    yield


app = FastAPI(
    title="Iris prediction API",
    description="An API that predicts iris species",
    version="1.0.0",
    lifespan=lifespan,
)


# Health check (Aliveness)
@app.get("/health")
def health():
    return {"status": "Health ok"}


# Readiness check
@app.get("/ready")
def ready(model=Depends(get_model)):
    if model is None:
        return {"status": "Model not ready"}

    return {"status": "Model ok"}


@app.post("/predict", response_model=List[int])
def predict(iris_features: IrisVariables, model=Depends(get_model)):

    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    data = [
        [
            iris_features.s_length,
            iris_features.s_width,
            iris_features.p_length,
            iris_features.p_width,
        ]
    ]

    predictions = model.predict(data).tolist()
    return predictions
