FROM python:3.7

RUN pip install -r requirements.txt

WORKDIR /usr/src

COPY data_access/ .

EXPOSE 8000

CMD ["gunicorn", "--access-logfile", "--error-logfile", "-", "--workers=2", "-b0.0.0.0:8000", "wsgi:app"]