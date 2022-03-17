from flask import Flask, jsonify, json, request
from flask_cors import CORS,cross_origin
import sys
import main
from base64 import b64encode
import json
import numpy
app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def home():
    return jsonify({'Error':'Request sent to invalid path'})

@app.route('/video', methods=['POST'])
@cross_origin()
def send_video():

    input = request.get_json()['data']
    video = main.build_video(input)
    file = open('final.mp4','rb')
    file.seek(0)
    data = b64encode(file.read())
    base64_string = data.decode('utf-8')
    raw_data = {'video':base64_string}
    data = json.dumps(raw_data)
    return data
