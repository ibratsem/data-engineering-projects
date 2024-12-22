# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the script and dependencies
COPY stream_kafka.py .
COPY requirements.txt .
COPY datasets/sales_data_sample.csv .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script when the container starts
CMD ["python", "stream_kafka.py"]
