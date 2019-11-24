from flask import Flask, jsonify, request
from app.producer import publish
import pika



def create_app():
    app = Flask(__name__)

    @app.route('/')
    def add_command():
        print("Request json is {}".format(request.get_json()))
        command = request.get_json()["data"]
        publish(command, "jobmanager")
        return jsonify("command <<{}>> published".format(command))
    return app



if __name__ == '__main__':
    app = create_app()
    app.run(port=8000)