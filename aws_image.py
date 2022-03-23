import boto3
from PIL import Image, ImageDraw, ImageFont
import io
import os
from dotenv import load_dotenv

def import_image(props):
    load_dotenv()
    s3 = boto3.client("s3", 
                  region_name=os.getenv('S3_REGION'),
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))
    
    images= []
    for i in range (len(props)):
        list = []
        list.append(props[i]['img_front'])
        list.append(props[i]['img_back'])
        list.append(props[i]['img_name'])
        
        image_dict = {}
        for j in range (len(list)):
            
            response = s3.get_object(Bucket = 'mpmedicinedb', Key = list[j])
            image_data = response['Body'].read()
            image = Image.open(io.BytesIO(image_data))
            image_dict[j] = image
        images.append(image_dict)
    return images


if __name__ == "__main__":
    input = "[{'id': '1644402640913', 'data': {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5',  'language': 'Marathi','ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}}, {'id': '1644402655353', 'data': {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'language': 'English', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}}]"
    import_image(input)



