FROM python:3.9.18

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install --upgrade pip

# Set the working directory in the container
WORKDIR /django

COPY ./notify.py /
COPY ./requirements_notify.txt /django/
RUN pip install -r requirements_notify.txt
COPY ./notify.py /django/

RUN echo "Construyendo para python"
COPY ./requirements.txt /django/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /porcigest
COPY . /django/

# Expose port 8000
EXPOSE 8000

# Update the command to use the correct path
# CMD python porcigest/manage.py runserver 0.0.0.0:8000 
CMD ["sh", "entrypoint.sh"]
