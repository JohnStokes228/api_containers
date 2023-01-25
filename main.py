import joblib
from fastapi import (
    FastAPI,
    Path
)
from typing import Dict
from utils.data_models import RequestBody
from utils.io_manager import IOManager
from train import NonsenseModel

app = FastAPI()
model = IOManager().read()


@app.get('/predict/{model_name}')
def make_prediction(
    request_message: RequestBody,
    model_name: str = Path('', description='name of the model you want to use to make predictions with')
):
    model.predict(X=request_message)

    return request_message
