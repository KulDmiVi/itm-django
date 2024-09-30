FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /myshop
COPY requirements.txt /myshop/
COPY run.sh  /myshop/
COPY ./myshop /myshop/

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Set entrypoint
#ENTRYPOINT bash ./myshop/run.sh
