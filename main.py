from fastapi import (
    FastAPI,
    Path
)
from typing import Dict
from utils.data_models import RequestBody

app = FastAPI()


@app.get('/predict/{model_name}')
def make_prediction(
    request_message: RequestBody,
    model_name: str = Path('', description='name of the model you want to use to make predictions with')
):
    request_message['predicted_cost'] = 1_400
    return request_message
