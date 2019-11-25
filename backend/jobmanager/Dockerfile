FROM python:3.7

WORKDIR /usr/src

COPY jobmanager/ .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


EXPOSE 8000

CMD [ "python", "-u", "manager.py" ]