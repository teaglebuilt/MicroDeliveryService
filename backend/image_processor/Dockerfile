FROM python:3.7

RUN pip install -r requirements.txt

WORKDIR /usr/src

COPY image_processor/ .

EXPOSE 8000

CMD [ "python", "-u", "image_collector.py" ]