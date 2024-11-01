FROM python:3.12

WORKDIR /ACM_SIGAI
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /ACM_SIGAI
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]





