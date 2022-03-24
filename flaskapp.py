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
            os.remove('mmp/'+patient_id+'.mp4')
            return jsonify({'OK':'The file has been successfully uploaded.'})
        except:
            return jsonify({'error':'Error encountered.Try again.'})
    else:
        return jsonify({'error':'The video generation failed.'})


@app.route('/get_mmp', methods=['POST'])
@cross_origin()
def get_video():

    patientId = request.get_json()['patientId']

    s3 = boto3.client(
        service_name='s3',
        region_name=REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_ACCESS_SECRET
    )

    bucket = 'mpmedicinedb'
    obj = 'generated_MP/'+patientId+'.mp4'

    response = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket':bucket,
            'Key':obj
        },
        ExpiresIn = 3600
    )

    return response
if __name__ == "__main__":
    app.run()


'''
{
    "data": [
        {
            "id": "1648029314708",
            "data": {
                "patientId": "60efb3be62512a00158190ca",
                "drug_name": "ADR_Carewin",
                "type": "Injections",
                "time": [
                    "Afternoon"
                ],
                "quantity": "2",
                "language": "Hindi",
                "ba": "before",
                "days": "1",
                "img_front": "MP_medicineDB/Injections/ADR_Carewin Pharmaceuticals_American Remedies_Front.jpg",
                "img_back": "MP_medicineDB/Injections/ADR_Carewin Pharmaceuticals_American Remedies_Back.jpg",
                "img_name": "MP_medicineDB/Injections/ADR_Carewin Pharmaceuticals_American Remedies_Name.jpg",
                "spcl_intr": ""
            }
        },
        {
            "id": "1648030523138",
            "data": {
                "patientId": "60efb3be62512a00158190ca",
                "drug_name": "Ibugem-400",
                "type": "Tablet",
                "time": [
                    "Morning",
                    "Afternoon"
                ],
                "quantity": "1",
                "language": "Marathi",
                "ba": "after",
                "days": "3",
                "img_front": "MP_medicineDB/Tablet/Ibugem-400 Tablets_Omega Pharma_Front.jpg",
                "img_back": "MP_medicineDB/Tablet/Ibugem-400 Tablets_Omega Pharma_Back.jpg",
                "img_name": "MP_medicineDB/Tablet/Ibugem-400 Tablets_Omega Pharma_Name.jpg",
                "spcl_intr": ""
            }
        }
    ]
}
'''