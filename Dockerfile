# Stage 1: Build Stage (Install Dependencies)
FROM python:3.9 AS builder
WORKDIR /app

# Install dependencies in a temporary layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production Stage (Final Slim Image)
FROM python:3.9-slim
WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . /app

# Expose Flask Port
EXPOSE 5000

# Start Flask App
CMD ["python", "run.py"]
