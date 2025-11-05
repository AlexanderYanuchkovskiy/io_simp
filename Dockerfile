FROM python:3.9-slim
WORKDIR /app
COPY io.py .
CMD ["python", "io.py"]