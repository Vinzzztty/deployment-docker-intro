FROM python:3.11-slim

# Workspace Directory
WORKDIR /app

# Install depedencies
RUN pip install fastapi uvicorn

COPY data /app/data
COPY ./main.py /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]