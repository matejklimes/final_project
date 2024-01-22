# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /gym

# Install dependencies
COPY requirements.txt /gym/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /gym/

# Make port 8000 available to the world outside this container
EXPOSE 8000