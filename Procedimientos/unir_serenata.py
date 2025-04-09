from moviepy import *


def union_clips_serenata(listsing):
    v1 = VideoFileClip(listsing[0])
    v2 = VideoFileClip(listsing[1])
    v3 = VideoFileClip(listsing[2])
    v4 = VideoFileClip(listsing[3])
    v5 = VideoFileClip(listsing[4])
    v6 = VideoFileClip(listsing[5])
    v7 = VideoFileClip(listsing[6])
    v8 = VideoFileClip(listsing[7])
    v9 = VideoFileClip(listsing[8])
    v10 = VideoFileClip(listsing[9])
    v11 = VideoFileClip(listsing[10])
    v12 = VideoFileClip(listsing[11])
    v13 = VideoFileClip(listsing[12])
    v14 = VideoFileClip(listsing[13])
    nombre = (listsing[14])

    union_clips = (f"Video final\Serenata para {nombre}.mp4")
    
    videosunidos = concatenate_videoclips(clips= [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14])

    videosunidos.write_videofile(union_clips, fps=30)

    return union_clips









