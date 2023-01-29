import uvicorn
from fastapi import (
    FastAPI
)
from typing import Dict
from utils.data_models import RequestBody
from utils.io_manager import IOManager

app = FastAPI()
model = IOManager().read()


@app.post("/predict")
def make_prediction(request_message: RequestBody) -> Dict[str, str]:
    predictions = model.predict(X=request_message)

    return predictions


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=8_000,
        host="0.0.0.0"
    )
