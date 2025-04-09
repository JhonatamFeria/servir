from moviepy import *
from PIL import *


#SOBREPONE EL NOMBRE DE LA HOMENAJEADA EN EL VIDEO DE DEDICAROTIA
def vid_intromotisere(intromotisere, nombre, estilo):
    clip_dedi = VideoFileClip(f"EstilosVideos\{intromotisere}").with_volume_scaled(1)
    duracion = clip_dedi.duration
    ima_estilo = ImageClip(estilo, transparent=True).with_duration(duracion)
    txt_clip_dedi = TextClip(font = "font\Lobster-Regular.ttf",
                             text = nombre,
                             font_size= 120,
                             color = "white",
                             stroke_width=3,
                             stroke_color="black",
                             horizontal_align = "center",
                             size = (1280, 720),
                             margin = (10, 280, 10, 10)
                             ).with_duration(duracion)
    videofinal_dedi = CompositeVideoClip([clip_dedi, ima_estilo, txt_clip_dedi]).with_effects([vfx.FadeIn(1), vfx.FadeOut(1),])
    videofinal_dedi.write_videofile(f"temp\{intromotisere}")
    return (f"temp\{intromotisere}")