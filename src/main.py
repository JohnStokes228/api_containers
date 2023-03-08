import uvicorn
from fastapi import (
    FastAPI
)
from typing import Dict
from utils.data_models import (
    RequestBody,
    ResponseMessage,
)
from utils.io_manager import IOManager

app = FastAPI()
model = IOManager().read()


@app.post("/predict")
def make_prediction(request_message: RequestBody) -> str:
    prediction = model.predict(X=request_message)
    response = ResponseMessage(**request_message.dict(), prediction=prediction)

    return response.json()


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=8_000,
        host="0.0.0.0"
    )
