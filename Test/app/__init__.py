from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import os
import sys

app = Flask(__name__)
api = Api(app)

class ChessPieces(Resource):
    def get(self, todo_id):
        path = '/static/images/chesspieces/wikipedia/' + todo_id
        #print(os.path.dirname(sys.modules['__main__'].__file__))
        print(path)
        return path

api.add_resource(ChessPieces, '/static/images/chesspieces/wikipedia/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

from app import routes
