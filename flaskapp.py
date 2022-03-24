from flask import Flask, jsonify, json, request,send_file
from flask_cors import CORS,cross_origin
import sys
import main
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_ACCESS_SECRET = os.getenv('AWS_SECRET_KEY')
REGION = os.getenv('S3_REGION')

app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def home():
    return jsonify({'Error':'Request sent to invalid path'})

@app.route('/upload_video', methods=['POST'])
@cross_origin()
def send_video():

    input = request.get_json()['data']
    patient_id = input[0]['data']['patientId']
    video = main.build_video(input)

    s3 = boto3.resource(
        service_name='s3',
        region_name=REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_ACCESS_SECRET
    )
    if video:
        bucket = s3.Bucket('mpmedicinedb')
        try:
            bucket.upload_file(Filename='mmp/'+patient_id+'.mp4', Key='generated_MP/'+patient_id+'.mp4')
            return jsonify({'OK':'The file has been successfully uploaded.'})
        except:
            return jsonify({'error':'Error encountered.Try again.'})
    else:
        return jsonify({'error':'The video generation failed.'})


if __name__ == "__main__":
    app.run()
