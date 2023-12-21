
from moviepy.editor import *
import moviepy as mp
from mutagen.mp3 import MP3
import random
from pymediainfo import MediaInfo

backs = ["back.mp4", "back2.mp4","back3.mp4","back4.mp4","back5.mp4","back6.mp4"]
a = MP3("audio.mp4")

clip1 = VideoFileClip(random.choice(backs))
audio = AudioFileClip("audio.mp4")
clip1 = clip1.set_audio(audio)
clip1 = clip1.fx(vfx.colorx, 0.8)
clip1 = clip1.crop(width=1080, height=1920)
overlay_clip = VideoFileClip(("audio.mp4"), has_mask=True, target_resolution=(720, 1280)) #.mov file with alpha channe
overlay_clip = vfx.mask_color(overlay_clip, color=[0,0,0])
overlay_clip = overlay_clip.set_position(("center"))
final_video = CompositeVideoClip([clip1, overlay_clip])

final_video.write_videofile("new.mp4")

