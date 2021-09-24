from moviepy.editor import *

clip = VideoFileClip("reagan.mp4")

clip = VideoFileClip("reagan.mp4").subclip(20, 30)
clip2 = VideoFileClip("reagan.mp4").subclip(35, 43)
clip3 = VideoFileClip("reagan.mp4").subclip(90, 104)
clip3 = VideoFileClip("reagan.mp4").subclip(107, 118)
clip4 = VideoFileClip("reagan.mp4").subclip(124, 128)
clip5 = VideoFileClip("reagan.mp4").subclip(189, 196)


final_clip = concatenate_videoclips([clip, clip2,clip3,clip4,clip5])


final_clip.write_videofile("edited.mp4")
