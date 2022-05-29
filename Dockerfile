# Dockerfile: Blueprint for building images
FROM python:3.9.9

WORKDIR /DuckDuckGo-Search-UI

# Adding Google Chrome trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome stable version to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating the repositories to see the stable version in apt and install Google Chrome
RUN apt-get -y update

# Installing google-chrome-stable
RUN apt-get install -y google-chrome-stable

# Installing unzip as we will need for the zipped Chrome Driver
RUN apt-get install -yqq unzip

# Download the Chrome Driver into a folder called /tmp/chromedriver.zip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

# Unzipping the Chrome Driver /tmp/chromedriver.zip into the Linux executable path into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable as Selenium is using this. It will avoid some crushes.
ENV DISPLAY=:99

# Install Python env requirements
RUN pip install --upgrade pip
# RUN pip list --format=freeze > requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m", "pytest"]



# Notes/Comments:

# Image: Template for running Containers
# Run this on the terminal to build image: docker build -t pytest-duckduckgo-search .

# Container: Actual running process where we have our package
# Run this on the terminal to start the container: docker run pytest-duckduckgo-search