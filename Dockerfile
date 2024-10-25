# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and script
COPY requirements.txt .
COPY i.py .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the bot
CMD ["python", "i.py"]
