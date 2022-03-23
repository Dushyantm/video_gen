from PIL import Image, ImageDraw, ImageFont

def buildImages(list, images ,text):
    myFont = ImageFont.truetype('font/Roboto-Regular.ttf', 65)
    myFont1 = ImageFont.truetype('font/Roboto-Bold.ttf', 65)
    MaHiFont = ImageFont.truetype('font/Nirmala.ttf', 65)
    frames = []

    for i in range (len(list)):
        drug_name = str(list[i]['drug_name'])
        text_str = str(text[i])
        bg_image = Image.new("RGB", (1920,1080), (255, 255, 255))
        frnt1 = images[i][0]
        back1 = images[i][1]
        name1 = images[i][2]
        newsize = (350,350)
        name_size = (250,100)
        frnt1 = frnt1.resize(newsize)
        back1 = back1.resize(newsize)
        name1 = name1.resize(name_size)
        f1 = ImageDraw.Draw(bg_image)        
        f1.text((700,120), drug_name, font=myFont1,fill=(255,0,0))
        #condition to check language and use font accordingly.
        if(list[i]['language']=='Hindi'):
            f1.text((950, 230), text_str, font=MaHiFont, fill=(0, 0, 0))
        if(list[i]['language']=='Marathi'):
            f1.text((950, 230), text_str, font=MaHiFont, fill=(0, 0, 0))
        else:
            f1.text((950, 230), text_str, font = myFont,  fill =(0, 0, 0))
        Image.Image.paste(bg_image, frnt1, (120,250))
        Image.Image.paste(bg_image, back1, (470,250))
        Image.Image.paste(bg_image, name1, (300,610))
        # bg_image.show()
        # bg_image.save('img2')
        frames.append(bg_image)
        
    return frames


# from text_script import getSentence
# from aws_image import import_image


# input = [{'id': '1644402640913', 'data': {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5',  'language': 'Marathi','ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}}, {'id': '1644402655353', 'data': {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'language': 'English', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}}]

# def build_video(input):
#     list = []
#     for i in range (len(input)):
#         dict = input[i] 
#         data = dict["data"]
#         list.append(data)
    
#     #fetch drug images
#     aws_image = import_image(list)

#     #generate text
#     text = getSentence(list)

#     #use drug images and text to build frames
#     print(buildImages(list, aws_image,text))

# print(buildImages(list, aws_image, text))