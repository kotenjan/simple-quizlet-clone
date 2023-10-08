FROM python:3.9

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

# Python, Selenium, and webdriver_manager
RUN pip install ipykernel selenium webdriver_manager

# Copy the code
COPY . /app
WORKDIR /app
