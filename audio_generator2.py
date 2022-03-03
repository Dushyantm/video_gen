from moviepy.editor import concatenate_audioclips,AudioFileClip
import os
import gtts



def audio_clip(meds,sentences):
    audio_clips = []

    for i in range(len(meds)):
        lang = meds[i]['language']

        #return audio according to language
        if lang == 'English':
            audio_clips.append(english_audio(meds[i]))
        if lang == 'Marathi':
            audio_clips.append(marathi_audio(sentences[i]))
        if lang == 'Hindi':
            audio_clips.append(hindi_audio(sentences[i]))

    return audio_clips

def english_audio(med):
    num2words = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}



    # Extract data from input
    time = [i[0].lower() for i in med['time']]
    time = ''.join(time)
    ba = med['ba'][:3]
    quantity = num2words[med['quantity']] + "_tablets"
    days = med['days']

    # get audio clip paths
    audio_path = ['recordings/' + quantity + '.wav', 'recordings/B_2.wav',
                  'recordings/' + time + "_" + ba + "_meal" + '.wav', 'recordings/D_4.wav',
                  'recordings/' + 'days_' + days + '.wav']

    # concatenate clips
    clips = [AudioFileClip(c) for c in audio_path]
    final_clip = concatenate_audioclips(clips)
    # append stitched audio clip
    return final_clip

def hindi_audio(sentence):

    # use gtts to generate text to speech
    tts = gtts.tts.gTTS(sentence,lang='hi',slow=True)

    # save the file
    tts.save('result.wav')

    # make a Moviepy clip from the file
    clip = AudioFileClip('result.wav')


    # append the generated audio

    return clip

def marathi_audio(sentence):


    # use gtts to generate text to speech
    tts = gtts.tts.gTTS(sentence,lang='mr',slow=True)

    # save to file
    tts.save('result.wav')

    # make a Moviepy clip from the file
    clip = AudioFileClip('result.wav')

    # remove the file to save space


    # append the generated audio cli
    return clip
