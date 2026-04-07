FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into /app
COPY . .

# Ensure database directory exists
RUN mkdir -p /app/data

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# app.py is in root directory, run it directly
CMD ["python", "app.py"]