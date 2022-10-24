from flask import Flask
from flask_restful import Api, Resource
from constants import server_ip, server_port
import pandas as pd

# data = pd.read_csv('math_students.csv', delimiter=',')
# data_apple = pd.read_csv('datasets//s&p500//AAPL.csv')


class Main(Resource):
    def get(self, company):
        if company == "0":
            data = pd.read_csv('math_students.csv', delimiter=',')
            return data.to_json(orient="records")
        else:
            data = pd.read_csv(f'datasets//s&p500//{company}.csv', delimiter='\\')
            return data.to_json(orient="records")



app = Flask(__name__)
api = Api()
api.add_resource(Main, "/api/info/<company>")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
