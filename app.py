from flask import Flask, request, jsonify
from main import get_assignments
app = Flask(__name__)
@app.route('/api/get_assignments')
def home():
    result=get_assignments()
    return jsonify(result)
    # return render_template('pages/placeholder.home.html')
if __name__ == '__main__':
    app.run()
