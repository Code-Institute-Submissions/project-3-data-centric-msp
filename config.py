""" This config file is used by the the memory game itself """

import os
from flask import Flask
from flask_pymongo import PyMongo

secret_key = os.getenv('secret_key')

""" Explicit check for environment to use the production or dev database database """
if os.getenv('C9_HOSTNAME'):
    mongodb = os.getenv('mongodb_dev')
else:
    mongodb = os.getenv('mongodb_prod')
    
""" Flask base information """
app = Flask(__name__)
app.config["MONGO_URI"] = mongodb
mongo = PyMongo(app)
