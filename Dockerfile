FROM python:3.9-alpine
ENV PYTHONBUFFERED=1
WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY . /usr/src/app/
EXPOSE 8000