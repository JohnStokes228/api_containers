FROM python:3.10.2

WORKDIR /fastapi-dummy

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src

CMD ["python", "./src/main.py"]