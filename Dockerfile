# Use an official Python runtime as a parent image
FROM python:3.7-alpine

# install dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Set the working directory to /app
ADD . /code
WORKDIR /code

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD python app.py
