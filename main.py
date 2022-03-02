from PIL import Image, ImageDraw
from audio import audio_clip
from text_script import getSentence
from aws_image import import_image
from buildImage import buildImages
from video import videoGen


input = [{'id': '1644402640913', 'data': {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5',  'language': 'Marathi','ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}}, {'id': '1644402655353', 'data': {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'language': 'English', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}}]

def build_video(input):
    list = []
    for i in range (len(input)):
        dict = input[i] 
        data = dict["data"]
        list.append(data)
    
    #fetch drug images
    aws_image = import_image(list)

    #generate audio
    audio_list = audio_clip

    #generate text
    text = getSentence(list)

    #use drug images and text to build frames
    frames = buildImages(list, aws_image,text )

    final_video = videoGen(frames,audio_list)
    
build_video(input)