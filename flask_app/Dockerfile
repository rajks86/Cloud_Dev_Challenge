# Use Python3
FROM python:3.9-slim

# Set up an app directory
COPY . /app
WORKDIR /app

# Install `pip` and needed Python packages from `requirements.txt`
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install -r requirements.txt
RUN apt-get autoremove -y gcc

EXPOSE 80

CMD ["python", "app.py"]