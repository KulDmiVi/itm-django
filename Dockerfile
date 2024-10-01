FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT=/itm-django/myshop
WORKDIR /itm-django
COPY requirements.txt /itm-django/
COPY run.sh  /itm-django/
COPY ./myshop /itm-django/

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR ${APP_ROOT}
# Set entrypoint
#ENTRYPOINT bash ./myshop/run.sh
