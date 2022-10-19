from flask import Flask
from flask_restful import Api, Resource
from constants import server_ip, server_port


class Main(Resource):
    def get(self):
        return {"version": 0.1, "name": "salt"}


app = Flask(__name__)
api = Api()
api.add_resource(Main, "/api/info")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)