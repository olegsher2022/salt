from flask import Flask, request
from flask_restful import Api, Resource
from helpers.constants import server_ip, server_port


class Main(Resource):
    def get(self):
        return {"version": 0.1, "name": "salt"}


app = Flask('my salt api server')
api = Api()
api.add_resource(Main, "/api/info")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=f'{server_port}', host=f'{server_ip}')
