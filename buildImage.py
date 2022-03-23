from PIL import Image, ImageDraw, ImageFont


def buildImages(list, images ,text):
    myFont = ImageFont.truetype('font/Roboto-Regular.ttf', 65)
    myFont1 = ImageFont.truetype('font/Roboto-Bold.ttf', 65)
    MarathiFont = ImageFont.truetype('font/Nirmala.ttf', 65)
    HindiFont = ImageFont.truetype('font/Mangal_Regular.ttf',65)
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
            f1.text((950, 230), text_str, font=HindiFont, fill=(0, 0, 0))
        if(list[i]['language']=='Marathi'):
            f1.text((950, 230), text_str, font=MarathiFont, fill=(0, 0, 0))
        else:
            f1.text((950, 230), text_str, font = myFont,  fill =(0, 0, 0))
        Image.Image.paste(bg_image, frnt1, (120,250))
        Image.Image.paste(bg_image, back1, (470,250))
        Image.Image.paste(bg_image, name1, (300,610))
        # bg_image.show()
        #bg_image.save('img'+str(i)+'.png')
        frames.append(bg_image)
        
    return frames

if __name__ == "__main__":
    pass