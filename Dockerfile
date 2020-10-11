FROM arm32v7/python:3.10.0a1-buster

COPY app/main.py ./app

RUN pip install --no-cache-dir rpi.gpio

CMD ["python", "./app/main.py"]