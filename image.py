from tkinter import font
from PIL import Image, ImageDraw, ImageFont
import textwrap

def buildImage():
    image = Image.new("RGB", (1920,1080), (255, 255, 255))
    frnt1 = Image.open(r"images\img0.jpg") 
    back1 = Image.open(r"images\img1.jpg")
    name1 = Image.open(r"images\img2.jpg")
    newsize = (350,350)
    name_size = (250,100)
    frnt1= frnt1.resize(newsize)
    back1= back1.resize(newsize)
    name1 = name1.resize(name_size)
    d1 = ImageDraw.Draw(image)
    myFont = ImageFont.truetype('font/Roboto-Regular.ttf', 65)
    myFont1 = ImageFont.truetype('font/Roboto-Bold.ttf', 65) 
    d1.text((700,120),"Norcin 400",font=myFont1,fill=(255,0,0))
    d1.text((950, 230), "Two tablets should be taken \nin the morning and evening \nafter your meal. \nThis tablet should be taken for \nten days.", font = myFont,  fill =(0, 0, 0))
    Image.Image.paste(image,frnt1,(120,250))
    Image.Image.paste(image,back1,(470,250))
    Image.Image.paste(image,name1,(300,610))
    image.save('img1.png')
    image.show()

buildImage()