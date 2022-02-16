from PIL import Image, ImageDraw, ImageFont


def buildImage():
    image = Image.new("RGB", (1920,1080), (255, 255, 255))
    frnt1 = Image.open(r"images\img0.jpg") 
    back1 = Image.open(r"images\img1.jpg")
    name1 = Image.open(r"images\img5.jpg")
    newsize = (350,350)
    name_size = (250,100)
    frnt1= frnt1.resize(newsize)
    back1= back1.resize(newsize)
    name1 = name1.resize(name_size)
    # d1 = ImageDraw.Draw(image)
    # d1.text((0, 0), "Sample text", fill =(255, 0, 0))
    Image.Image.paste(image,frnt1,(120,200))
    Image.Image.paste(image,back1,(470,200))
    Image.Image.paste(image,name1,(300,560))
    # print(props)
    image.show()

buildImage()