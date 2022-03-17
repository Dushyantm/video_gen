from flask import Flask, jsonify, json, request
from flask_cors import CORS,cross_origin
import sys
import main
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
    video = numpy.array(main.build_video(input))
    file = {"video":"video generated"}
    return jsonify(file)
