from flask import Flask, request, jsonify
from main import get_assignments
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/api/get_assignments')
@cross_origin()
def home():
    result=get_assignments()
    return jsonify(result)
    # return render_template('pages/placeholder.home.html')
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)
