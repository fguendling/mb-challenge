FROM python:3.11-slim

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

