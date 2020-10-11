FROM arm32v7/python:3.10.0a1-buster

RUN pip install --no-cache-dir rpi.gpio

COPY ./app /app

CMD ["python", "/app/main.py"]