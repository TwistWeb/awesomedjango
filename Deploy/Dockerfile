FROM python:3.8
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt && \
    python3 manage.py migrate
CMD ['python3', 'manage.py', 'runserver', '0.0.0.0:8000']
