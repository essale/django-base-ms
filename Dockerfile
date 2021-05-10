FROM python:3.9 AS compile-image
ENV PYTHONUNBUFFERED=1
workdir /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD python manage.py runserver 0.0.0.0:8000