from moviepy.editor import *
import numpy as np
import glob
import cv2


def changevideo_res_speed(video,output):
    cap = cv2.VideoCapture(video)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output,fourcc, 80, (1080,1920))

    while True:
        ret, frame = cap.read()
        if ret == True:
            b = cv2.resize(frame,(1080,1920),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            out.write(b)
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


#changevideo_res_speed('./speed_videos/20210308_082705.mp4')


#################################################################

#speed_num = int(input("Enter the speed of your videos : "))
#
# videos_arr   =  []
# speed_videos =  []
#
# for videoname in glob.glob('./videos/*.mp4'):
#     videos_arr.append(videoname)
#

def speedup():
    i = 0
    for videospeed in glob.glob('./speed_videos/*.mp4'):
        # speed_videos.append(videospeed)
        # cap = VideoFileClip(videospeed)
        # final = cap.fx( vfx.speedx, speed_num)
        path_name = "./work/speed" + str(i) + ".mp4"
        changevideo_res_speed(videospeed,path_name)
        #final.write_videofile(path_name)
        i= i+1

#speedup()


# total = i + len(videos_arr)

 # clip0 = VideoFileClip("./work/speed0.mp4")
 # clip1 = VideoFileClip("./work/speed1.mp4")
 # clip2 = VideoFileClip("./videos/1.mp4")
 # clip3 = VideoFileClip("./work/speed2.mp4")
 # clip4 = VideoFileClip("./work/speed3.mp4")
 # clip5 = VideoFileClip("./videos/2.mp4")
 # clip6 = VideoFileClip("./work/speed4.mp4")
 # clip7 = VideoFileClip("./work/speed5.mp4")
 # clip8 = VideoFileClip("./videos/3.mp4")
 # clip9 = VideoFileClip("./work/speed6.mp4")
 # clip10 = VideoFileClip("./work/spee7.mp4")
 # clip11 = VideoFileClip("./videos/4.mp4")
 # clip12 = VideoFileClip("./work/speed8.mp4")

#
#
#
 # final_clip = concatenate_videoclips([clip0 ,clip1 ])
#
#
 # final_clip.write_videofile("final.mp4")

def getVideoRes(video):
    vcap = cv2.VideoCapture(video)
    if vcap.isOpened():
        width  = vcap.get(3)  # float `width`
        height = vcap.get(4)  # float `height
        return (width,height)



#getVideoRes('./1.mp4')

def getVideo_frame(video):
    vcap = cv2.VideoCapture(video)
    if vcap.isOpened():
        framespersecond= int(vcap.get(cv2.CAP_PROP_FPS))
        return framespersecond

############################################################################

#cv2 soluction
def edit_my_videos():
    fps = 50
    #resolution = (1366,768)
    resolution = (1080,1920)

    #videos = ["./work/speed0.mp4","./videos/reagan1.mp4","./work/speed1.mp4","./videos/reagan2.mp4"]
    videos = ["./work/speed0.mp4",
             "./work/speed1.mp4",
             "./videos/1.mp4",
             "./work/speed2.mp4",
             "./work/speed3.mp4",
             "./videos/2.mp4",
             "./work/speed4.mp4",
             "./work/speed5.mp4",
             "./videos/3.mp4",
             "./work/speed6.mp4",
             "./work/speed7.mp4",
             "./videos/4.mp4",
             "./work/speed8.mp4"
             ]
    video = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"MPEG"), fps, resolution)


    for v in videos:
        curr_v = cv2.VideoCapture(v)
        while curr_v.isOpened():
            r, frame = curr_v.read()    # Get return value and curr frame of curr video
            if not r:
                break
            video.write(frame)          # Write the frame

    video.release()



#edit_my_videos()

############################################################################################



def add_music(video,audio):
    video1 = VideoFileClip(video)
    audio = AudioFileClip(audio)
    final = video1.set_audio(audio)
    final.write_videofile("final_output.mp4")

    return

add_music('me.mp4','./music/fiji.mp3')

##################################################################

def change_speed():
    in_loc = './speed_videos/20210308_082705.mp4'
    out_loc = 'dummy_out.mp4'

    # Import video clip
    clip = VideoFileClip(in_loc)
    print("fps: {}".format(clip.fps))

    # Modify the FPS
    clip = clip.set_fps(clip.fps * 3)

    # Apply speed up
    final = clip.fx(vfx.speedx, 3)
    print("fps: {}".format(final.fps))

    # Save video clip
    final.write_videofile(out_loc)


#change_speed()
############################################################""





#changevideo_res()
# print(videos_arr)
# print('\n')
# print(speed_videos)
