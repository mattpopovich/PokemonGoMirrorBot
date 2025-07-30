### This Dockerfile is only for code development and unit testing.
### Cliclick is needed to run the scripts, and that is only available on macOS.

# Get current python image
FROM python:3.12.11-bullseye

# Update image
RUN apt-get update && apt-get upgrade -y

# Unit testing
RUN pip3 install --upgrade pytest

# ImageGrab
RUN pip3 install --upgrade pillow

# Set working directory
WORKDIR /app

# Copy my project code into the image
COPY . .
