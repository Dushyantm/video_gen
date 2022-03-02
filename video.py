from moviepy.editor import *
import text_script
import audio_generator2
from PIL import Image
import numpy as np


#this function changes the PIL image to numpy array
def image_to_array(frames):
    rgb_frames = [i.convert('RGB') for i in frames]
    frames_array = [np.array(i).reshape(i.size[1],i.size[0],3) for i in rgb_frames]

    return frames_array

def video_generator(frames,audio_clips):

    #frames = [Image.open(i) for i in frames]
    frames_array = image_to_array(frames)

    video_clips = []


    for i in range(len(frames_array)):

        #create infinite long Image clip
        clip = ImageClip(frames_array[i])

        #set duration and audio_clip
        clip = clip.set_duration(audio_clips[i].duration+1)
        clip = clip.set_audio(audio_clips[i])

        video_clips.append(clip)

    #concatenate the video clips
    final = concatenate_videoclips(video_clips,method='compose')
    #final.write_videofile('final.mp4',fps=1)

    return final


#the below code is for module tests only
input = [{'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5', 'language': 'Marathi', 'ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}, {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Afternoon'], 'quantity': '2', 'language': 'English', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}]

frames = ['img1.png','img2.png']
sentences = text_script.getSentence(input)
audio_clips = audio_generator2.generate_audio(input,sentences)

video_generator(frames,audio_clips)

