# Use Python 3 as the base image
FROM python:alpine

# Set working directory
WORKDIR /shell

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the shell program
COPY . .

# Set the entry point
CMD ["python", "shell.py"] 