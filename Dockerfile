# set base image (host OS)
FROM python:3.10.0b3-slim-buster

# set the working directory in the container
WORKDIR /ishibashitracker

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local directory to the working directory
COPY . .

# command to run on container start
CMD [ "python3", "main.py" ]