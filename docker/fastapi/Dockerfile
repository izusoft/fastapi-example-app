FROM python:3.8.1

ENV PYTHONUNBUFFERED 1

WORKDIR /var/www

COPY . /var/www

RUN pip install -r "/var/www/requipments.txt"

EXPOSE 5000

CMD ["python", "/var/www/app/main.py"]