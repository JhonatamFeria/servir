from moviepy import *
from PIL import *

#SOBREPONE EL NOMBRE DE LA HOMENAJEADA EN EL VIDEO DE LAS PALABRAS
def vid_videopalabras(videopalabras, nombre, estilo):
    clip_pala = VideoFileClip(f"tempcli\{videopalabras}").with_volume_scaled(1).with_effects([vfx.Resize((1280,720))]).with_fps(30)
    duracion = clip_pala.duration
    ima_estilo = ImageClip(estilo, transparent=True).with_duration(duracion)
    txt_clip_pala = TextClip(font = "font\Lobster-Regular.ttf",
                             text = nombre,
                             font_size= 120,
                             color = "white",
                             stroke_width=3,
                             stroke_color="black",
                             horizontal_align = "center",
                             size = (1280, 720),
                             margin = (10, 280, 10, 10)
                             ).with_duration(duracion)
    videofinal_pala = CompositeVideoClip([clip_pala, ima_estilo, txt_clip_pala]).with_effects([vfx.FadeIn(1), vfx.FadeOut(1),])
    videofinal_pala.write_videofile(f"temp\{videopalabras}")
    return (f"temp\{videopalabras}")
     