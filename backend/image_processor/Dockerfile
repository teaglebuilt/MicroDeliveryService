FROM python:3.7

WORKDIR /usr/src

COPY image_processor/ .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "-u", "image_collector.py" ]