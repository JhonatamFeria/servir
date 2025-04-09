from moviepy import *
from PIL import *


#SOBREPONE EL NOMBRE DE LA HOMENAJEADA EN LA CANCION 1
def vid_cancion1(cancion1, nombre, estilo):
    clip_c1 = VideoFileClip(f"CancionesVideos\{cancion1}").with_volume_scaled(1).with_effects([vfx.Resize((1280,720))]).with_fps(30)
    duracion = clip_c1.duration
    ima_estilo = ImageClip(estilo, transparent=True).with_duration(duracion)
    txt_clip_c1 = TextClip(font = "font\Lobster-Regular.ttf",
                           text = nombre,
                           font_size= 120,
                           color = "white",
                           stroke_width=3,
                           stroke_color="black",
                           horizontal_align = "center",
                           size = (1280, 720),
                           margin = (10, 280, 10, 10)
                           ).with_duration(duracion)
    videofinal_c1 = CompositeVideoClip([clip_c1, ima_estilo, txt_clip_c1]).with_effects([vfx.FadeIn(1), vfx.FadeOut(1),])
    videofinal_c1.write_videofile(f"temp\{cancion1}", fps=30)
    return (f"temp\{cancion1}")
    