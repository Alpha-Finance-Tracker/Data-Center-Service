# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Install Tesseract OCR, OpenCV, and other dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-bul \
    libleptonica-dev \
    libtesseract-dev \
    imagemagick \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8001 for the FastAPI app
EXPOSE 8001

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
