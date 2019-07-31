from flask import Flask, render_template, url_for
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import os
import sys

app = Flask(__name__)
api = Api(app)

class ChessPieces(Resource):
    def get(self, filename):
        path = '/static/images/chesspieces/wikipedia/' + filename
        print(path)
        return path

api.add_resource(ChessPieces, '/images/chesspieces/wikipedia/<path:filename>')

if __name__ == '__main__':
    app.run(debug=True)

from app import routes
