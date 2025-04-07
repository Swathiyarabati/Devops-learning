# Use the official Python image from the Docker Hub as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world (replace with the actual port your app uses)
EXPOSE 8000

# Run the main.py script when the container starts and keep the container running
CMD python main.py && tail -f /dev/null
