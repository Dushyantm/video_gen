from moviepy.editor import *
import text_script
from audio import audio_clip
from PIL import Image
import numpy as np
import glob

#this function changes the PIL image to numpy array
def image_to_array(list):
    rgb_frames = [i.convert('RGB') for i in list]
    frames_arr = [np.array(i).reshape(i.size[1],i.size[0],3) for i in rgb_frames]

    return frames_arr

def video_generator(audio_clips):

    #to get the medicine images
    list1 = ['d.png', 'c.png']
    list1 = [Image.open(i) for i in list1]

    #to get the starting images for every video
    list = []
    for img in glob.glob("framesFolder/*.png"):
        image = Image.open(img)
        list.append(image)

    #concatenate list and list1
    list.extend(list1)
    #append the last frame of the video
    list.append(Image.open('z.png'))

    video_clips = []

    frames_array = image_to_array(list)
    
    mp = ImageClip(frames_array[0])
    mp = mp.set_duration(3)
    video_clips.append(mp)

    intr1 = ImageClip(frames_array[1])
    intr1 = intr1.set_duration(2)
    video_clips.append(intr1)

    for i in range(len(audio_clips)):

        #create infinite long Image clip 
        clip = ImageClip(frames_array[i+2]) 

        #set duration and audio_clip for each image clip  
        clip = clip.set_duration(audio_clips[i].duration+1)
        clip = clip.set_audio(audio_clips[i])

        video_clips.append(clip)

   
    intr2 = ImageClip(frames_array[-1])
    intr2 = intr2.set_duration(4)
    video_clips.append(intr2) 
    
    #concatenate the video clips
    final = concatenate_videoclips(video_clips,method='compose')
    final.write_videofile('final.mp4',fps=1)

    return final

# video_generator(list, audio_clips)
