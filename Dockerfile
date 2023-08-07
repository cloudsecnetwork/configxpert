# Use the official Python image as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Install required Python packages from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Run the main.py script when the container starts
CMD ["python", "main.py"]
