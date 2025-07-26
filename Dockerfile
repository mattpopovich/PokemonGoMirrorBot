# Get current python image
FROM python:3.12.11-bullseye

# Update image
RUN apt-get update && apt-get upgrade -y

