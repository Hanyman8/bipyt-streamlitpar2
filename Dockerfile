FROM python:3.9-slim


WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install libgl1 -y

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .


EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]