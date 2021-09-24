from moviepy.editor import *
import numpy as np
import glob
import cv2

# speed_num = int(input("Enter the speed of your videos : "))
#
# videos_arr   =  []
# speed_videos =  []
#
# for videoname in glob.glob('./videos/*.mp4'):
#     videos_arr.append(videoname)
#
# i = 0
# for videospeed in glob.glob('./speed_videos/*.mp4'):
#     # speed_videos.append(videospeed)
#     cap = VideoFileClip(videospeed)
#     final = cap.fx( vfx.speedx, speed_num)
#     path_name = "./work/speed" + str(i) + ".mp4"
#     final.write_videofile(path_name)
#     i= i+1
#
#
# total = i + len(videos_arr)

# clip0 = VideoFileClip("./videos/reagan2.mp4")
# clip1 = VideoFileClip("./work/speed0.mp4")
# clip2 = VideoFileClip("./videos/reagan1.mp4")
# clip4 = VideoFileClip("./work/speed1.mp4")
#
#
#
# final_clip = concatenate_videoclips([clip0 ,clip1 ,clip2, clip4])
#
#
# final_clip.write_videofile("final.mp4")

#cv2 soluction

fps = 30
resolution = (1366,768)

videos = ["./work/speed0.mp4","./videos/reagan1.mp4","./work/speed1.mp4","./videos/reagan2.mp4"]
video = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"MPEG"), fps, resolution)


for v in videos:
    curr_v = cv2.VideoCapture(v)
    while curr_v.isOpened():
        r, frame = curr_v.read()    # Get return value and curr frame of curr video
        if not r:
            break
        video.write(frame)          # Write the frame

video.release()




def changevideo_res():
    cap = cv2.VideoCapture('./videos/reagan1.mp4')

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 30, (1366,768))

    while True:
        ret, frame = cap.read()
        if ret == True:
            b = cv2.resize(frame,(1366,768),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            out.write(b)
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()



#changevideo_res()
# print(videos_arr)
# print('\n')
# print(speed_videos)
