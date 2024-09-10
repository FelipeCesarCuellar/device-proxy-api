FROM python:3.11-alpine

# Install system dependencies
RUN apk update \
 && apk add --virtual build-deps gcc python3-dev musl-dev git \
 && apk add postgresql-dev \
 && pip3 install psycopg2 \
 && apk del build-deps

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
COPY src /app.
WORKDIR /app
EXPOSE 3000

# Run Gunicorn with your Falcon application
CMD ["gunicorn", "-w", "5", "-b", "0.0.0.0:3000", "app:api", "--timeout", "120"]
