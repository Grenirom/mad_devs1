FROM python:3.11-slim

# setting working directory
WORKDIR /app

# copy requirements.txt file
COPY requirements.txt .

# install all dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy project to containter
COPY . .

# run migrations and server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]