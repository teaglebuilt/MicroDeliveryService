from flask import Flask, jsonify, request, Response
from app.producer import publish
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import pika
import time




def create_app():
    app = Flask(__name__)

    INF = float("inf")

    graphs = {}
    graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
    graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, INF))


    @app.route('/')
    def add_command():
        print("Request json is {}".format(request.get_json()))
        start = time.time()
        command = request.get_json()["data"]
        publish(command, "jobmanager")
        end = time.time()
        graphs['h'].observe(end - start)
        return jsonify("command <<{}>> published".format(command))

    @app.route("/metrics")
    def requests_count():
        res = []
        for k,v in graphs.items():
            res.append(prometheus_client.generate_latest(v))
        return Response(res, mimetype="text/plain")

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(port=8000)