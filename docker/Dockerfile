FROM python:3.12.2-slim

# setting working directory
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# copy requirements.txt file
COPY ./requirements.txt .

# install all dependencies from requirements.txt
RUN pip install -r requirements.txt


# copy project to containter
COPY . .