import pickle 
import contextlib
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List    

class  IrisVariables (BaseModel):
    s_length: float
    s_width: float
    p_length: float
    p_width: float

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI): 
    global model   
    try : 
        with open("models/vanilla_model.pkl", "rb") as f:
            model = pickle.load(f)
    except FileNotFoundError:
        print ("Can't find file")
    except Exception as e:
        print (f"Error : {e}")
    yield

app = FastAPI(
    title = "Iris prediction API",  
    description = "An API that predicts iris species",
    version = "1.0.0",
    lifespan=lifespan
)

@app.post("/predict", response_model=List[int])
def predict(iris_features : IrisVariables):

    if not model:
        return {"error": "No model found"}
    
    data = [[
        iris_features.s_length,
        iris_features.s_width,
        iris_features.p_length,
        iris_features.p_width
    ]]

    predictions = model.predict(data).tolist()
    return predictions