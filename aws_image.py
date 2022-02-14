import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def import_image(props):
    
    s3 = boto3.client("s3", 
                  region_name='ap-southeast-1', 
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))
    list = props[0]
    print(list['img_back'])