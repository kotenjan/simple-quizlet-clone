FROM python:3.9

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

COPY requirements.txt .
RUN pip3 install -r requirements.txt
