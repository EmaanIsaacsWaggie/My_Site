# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/

# Expose the port your Django app will run on
EXPOSE 8000

# Command to run the Django app (adjust as needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
