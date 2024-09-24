FROM python:3.9-alpine
ENV PYTHONBUFFERED=1
RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["sh", "entrypoint.sh"]
