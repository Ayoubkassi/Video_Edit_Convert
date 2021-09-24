from moviepy.editor import *

#clip = VideoFileClip("reagan.mp4")

# clip = VideoFileClip("reagan.mp4").subclip(20, 30)
# clip2 = VideoFileClip("reagan.mp4").subclip(35, 43)
# clip3 = VideoFileClip("reagan.mp4").subclip(90, 104)
# clip3 = VideoFileClip("reagan.mp4").subclip(107, 118)
# clip4 = VideoFileClip("reagan.mp4").subclip(124, 128)
# clip5 = VideoFileClip("reagan.mp4").subclip(189, 196)

clip1 = VideoFileClip("edited.mp4")
clip2 = VideoFileClip("reagan2.mp4")


final_clip = concatenate_videoclips([clip1 , clip2])


final_clip.write_videofile("final.mp4")
