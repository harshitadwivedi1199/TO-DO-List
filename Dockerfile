# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the command to start the Flask app
CMD ["flask", "run"]
