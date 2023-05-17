import pymongo
from flask import Flask
from flask_restful import Api
from pymongo.server_api import ServerApi
import os

app = Flask(__name__)

conn = os.environ.get("MONGODB_CONN")

client = pymongo.MongoClient(conn, server_api=ServerApi('1'))

CarbonFree = client.CarbonFree

api = Api(app)

from application import routes
