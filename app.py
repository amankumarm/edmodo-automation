from flask import Flask, request, jsonify
from main import get_assignments
from flask_cors import CORS, cross_origin
from datetime import datetime
import os
import pickle
import json
import dill
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/update')
@cross_origin()
def home():
    result=get_assignments()
    with open('./cache/result.json','w') as fp:
        json.dump(result,fp)
    return jsonify(result)


@app.route('/api/get_assignments')
@cross_origin()
def get_assi():
    
    with open("./cache/result.json", "r") as json_file:
        data=json.load(json_file)
    return jsonify(data)




# if you are here later - remember
# cache folder must have a latest result .json file
