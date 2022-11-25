# Dockerfile

FROM python:3-slim

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY /project /code/project
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "project/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
