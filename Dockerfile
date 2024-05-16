# Use the latest Ubuntu LTS as base image
FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update package lists and install essential packages
RUN apt-get update \
    && apt-get install -y \
        python3.9 \
        python3-pip \
        nodejs \
        npm \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3.9 /usr/local/bin/python \
    && ln -s /usr/bin/pip3 /usr/local/bin/pip

# Set the working directory in the container
WORKDIR /django

# Copy the requirements file into the container at /porcigest
COPY ./requirements.txt /django/

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /porcigest
COPY . /django/

# Expose port 8000
EXPOSE 8000
