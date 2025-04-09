from moviepy import *
from PIL import *


#SOBREPONE EL NOMBRE DE LA HOMENAJEADA EN LA CANCION 3
def vid_cancion3(cancion3, nombre, estilo):
    clip_c3 = VideoFileClip(f"CancionesVideos\{cancion3}").with_volume_scaled(1).with_effects([vfx.Resize((1280,720))]).with_fps(30)
    duracion = clip_c3.duration
    ima_estilo = ImageClip(estilo, transparent=True).with_duration(duracion)
    txt_clip_c3 = TextClip(font = "font\Lobster-Regular.ttf",
                           text = nombre,
                           font_size= 120,
                           color = "white",
                           stroke_width=3,
                           stroke_color="black",
                           horizontal_align = "center",
                           size = (1280, 720),
                           margin = (10, 280, 10, 10)
                           ).with_duration(duracion)
    videofinal_c3 = CompositeVideoClip([clip_c3, ima_estilo, txt_clip_c3]).with_effects([vfx.FadeIn(1), vfx.FadeOut(1),])
    videofinal_c3.write_videofile(f"temp\{cancion3}", fps=30)
    return (f"temp\{cancion3}")

    