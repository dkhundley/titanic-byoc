# Instantiating the base image
FROM python:3.9-slim-buster

# Installing our dependencies
COPY dependencies/requirements.txt /
RUN pip install -r /requirements.txt

# Setting the environment variables required by AWS SageMaker
ENV PYTHONBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Exposing the proper port
EXPOSE 8080

# Moving the project files from local into Docker image
COPY models/ /opt/program
COPY container/ /opt/program

# Setting the working directory to be "opt/program/"
WORKDIR /opt/program