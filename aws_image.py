import boto3
from PIL import Image, ImageDraw, ImageFont
import io
import os
from dotenv import load_dotenv

load_dotenv()

input = [{'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5', 'ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}, {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}]

def import_image(props):

    s3 = boto3.client("s3", 
                  region_name='ap-southeast-1', 
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))
    
    
    for i in range (len(props)):
        list = []
        list.append(props[i]['img_front'])
        list.append(props[i]['img_back'])
        list.append(props[i]['img_name'])
        
        images= []
        for j in range (len(list)):
            
            response = s3.get_object(Bucket = 'mpmedicinedb', Key = list[j])
            image_data = response['Body'].read()
            image = Image.open(io.BytesIO(image_data))
            images.append(image)
            
        blank_img = Image.new("RGB", (1920,1080), (255, 255, 255))
        newsize = (450,450)
        frnt_img = images[1].resize(newsize)
        
        Image.Image.paste(blank_img,frnt_img,(450,450))
        # blank_img.show()

import_image(input)

