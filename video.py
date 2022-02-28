from moviepy.editor import *
import text_script
import audio_generator2

def video_generator(frames,audio_clips):

    video_clips = []

    for i in range(len(frames)):
        clip = ImageSequenceClip([frames[i]],fps=1)
        clip = clip.set_duration(audio_clips[i].duration)
        clip = clip.set_audio(audio_clips[i])

        video_clips.append(clip)









input = [{'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5', 'language': 'Marathi', 'ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}, {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Afternoon'], 'quantity': '2', 'language': 'English', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}]

sentences = text_script.getSentence(input)
audio_clips = audio_generator2.generate_audio(input,sentences)

frames = ['img1.png','img2.png']


video_generator(frames,audio_clips)

