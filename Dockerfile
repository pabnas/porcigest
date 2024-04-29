# Use an official Python runtime as a parent image
FROM python:3.9.18

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /django

# Copy the requirements file into the container at /porcigest
COPY ./requirements.txt /django/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /porcigest
COPY . /django/

# Expose port 8000
EXPOSE 8000


# Update the command to use the correct path
# CMD python porcigest/manage.py runserver 0.0.0.0:8000 
CMD ["sh", "entrypoint.sh"]