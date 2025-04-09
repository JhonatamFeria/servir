from moviepy import *
from PIL import *


#SOBREPONE EL NOMBRE DE LA HOMENAJEADA EN LA CANCION 1
def transicion_especial(texto, estilo_especial):
    ima_estilo = ImageClip(estilo_especial).with_duration(4)
    
    txt_clip_c1 = TextClip(font = "font\Lobster-Regular.ttf",
                           text = (f"{texto}"),
                           font_size= 60,
                           color = "white",
                           stroke_width=3,
                           stroke_color="black",
                           horizontal_align = "center",
                           size = (1280, 720),
                           text_align = "center"
                           ).with_duration(4)
    videofinal_c1 = CompositeVideoClip([ima_estilo, txt_clip_c1]).with_effects([vfx.FadeIn(1), vfx.FadeOut(1),])
    videofinal_c1.write_videofile(f"temp\{texto}.mp4", fps=30, audio=True)
    
    return (f"temp\{texto}.mp4")