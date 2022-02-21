from moviepy.editor import *

img = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png',
       '7.png', '8.png', '9.png', '10.png', '11.png', '12.png']

clips = [ImageClip(m).set_duration(2)
      for m in img]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=24)