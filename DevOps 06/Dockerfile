FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r news/requirements.txt

EXPOSE 8000

CMD ["python", "news/manage.py", "runserver", "0.0.0.0:8000"]
