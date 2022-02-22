from PIL import Image, ImageDraw, ImageFont

from text_script import text_script

input = [{'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5', 'ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}, {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}]
text = text_script(input)
text_str = str(text[1])
myFont = ImageFont.truetype('font/Roboto-Regular.ttf', 65)
myFont1 = ImageFont.truetype('font/Roboto-Bold.ttf', 65)
bg_image = Image.new("RGB", (1920,1080), (255, 255, 255))
frnt1 = Image.open(r"images\img0.jpg") 
back1 = Image.open(r"images\img1.jpg")
name1 = Image.open(r"images\img2.jpg")
newsize = (350,350)
name_size = (250,100)
frnt1= frnt1.resize(newsize)
back1= back1.resize(newsize)
name1 = name1.resize(name_size)
f1 = ImageDraw.Draw(bg_image)        
f1.text((700,120), "norcin", font=myFont1,fill=(255,0,0))
f1.text((950, 230), text_str, font = myFont,  fill =(0, 0, 0))
Image.Image.paste(bg_image,frnt1,(120,250))
Image.Image.paste(bg_image,back1,(470,250))
Image.Image.paste(bg_image,name1,(300,610))
bg_image.show()
