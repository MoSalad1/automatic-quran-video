from moviepy.editor import *
import random
a = ["quran1.mp4","quran2.mp4"]
b = VideoFileClip(random.choice(a))
b.write_videofile("audio.mp4")
