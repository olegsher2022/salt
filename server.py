from flask import Flask
from flask_restful import Api, Resource
from constants import server_ip, server_port
import pandas as pd

data = pd.read_csv('math_students.csv', delimiter=',')


class Main(Resource):
    def get(self):
        return data.to_json(orient="records")


app = Flask(__name__)
api = Api()
api.add_resource(Main, "/api/info")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
