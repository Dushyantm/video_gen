from flask import Flask, jsonify, json, request
from flask_cors import CORS,cross_origin
import sys
app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def home():
    return "Hello, Flask!"
@app.route('/sendjson', methods=['POST'])
@cross_origin()
def sendjson():

    data = json.loads(request.get_data())
    print(data, file=sys.stdout)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=6000, debug=True)