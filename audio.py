input = [{'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5', 'ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}, {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}]
from moviepy.editor import concatenate_audioclips,AudioFileClip
import os
import gtts

def audio_clip(meds,sentences):

    #get language from first record
    lang = meds[0]['language']

    #return audio according to language
    if lang == 'English':
        return english_audio(meds)
    if lang == 'Marathi':
        return marathi_audio(sentences)
    if lang == 'Hindi':
        return hindi_audio(sentences)


def english_audio(meds):
    num2words = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}

    audio_clips = []

    for medicine in meds:
        # Extract data from input
        time = [i[0].lower() for i in medicine['time']]
        time = ''.join(time)
        ba = medicine['ba'][:3]
        quantity = num2words[medicine['quantity']] + "_tablets"
        days = medicine['days']

        # get audio clip paths
        audio_path = ['recordings/' + quantity + '.wav', 'recordings/B_2.wav',
                      'recordings/' + time + "_" + ba + "_meal" + '.wav', 'recordings/D_4.wav',
                      'recordings/' + 'days_' + days + '.wav']

        # concatenate clips
        clips = [AudioFileClip(c) for c in audio_path]
        final_clip = concatenate_audioclips(clips)

        # append stitched audio clip
        audio_clips.append(final_clip)

    return audio_clips

def hindi_audio(sentences):


    audio_clips = []

    for sen in sentences:

        # use gtts to generate text to speech
        tts = gtts.tts.gTTS(sen,lang='hi',slow=True)

        # save the file
        tts.save('result.wav')

        # make a Moviepy clip from the file
        clip = AudioFileClip('result.wav')

        # delete the file to save space
        os.remove('result.wav')

        # append the generated audio
        audio_clips.append(clip)

    return audio_clips

def marathi_audio(sentences):


    audio_clips = []

    for sen in sentences:

        # use gtts to generate text to speech
        tts = gtts.tts.gTTS(sen,lang='mr',slow=True)

        # save to file
        tts.save('result.wav')

        # make a Moviepy clip from the file
        clip = AudioFileClip('result.wav')

        # remove the file to save space
        os.remove('result.wav')

        # append the generated audio clip
        audio_clips.append(clip)

    return audio_clips