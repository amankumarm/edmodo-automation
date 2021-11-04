from flask import Flask, request, jsonify
from main import get_assignments
from flask_cors import CORS, cross_origin
from datetime import datetime
import os
import pickle
import dill
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/get_assignments')
@cross_origin()
def home():
    # curr_time = datetime.now()
    # cached_time = dill.load(open("./cache/cache.pickle", "rb"))
    # difference = (curr_time-cached_time).total_seconds()
    # if(difference >= 600):
    #     print("more than 10 mins")
    # else:
    #     print("less than it")
    # return "heyy"
    result=get_assignments()
    return jsonify(result)
    return render_template('pages/placeholder.home.html')
