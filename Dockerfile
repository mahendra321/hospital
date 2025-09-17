# Use official Python image
FROM python:3
# Set working directory
WORKDIR /HOSPITAL_FULL_PROJECT

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ app/

# Expose FastAPI port
#EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "app.patient_registration:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
