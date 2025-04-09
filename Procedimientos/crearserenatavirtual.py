from moviepy import *
from PIL import *
from Procedimientos.intromotisere import vid_intromotisere
from Procedimientos.videofinalcancion1 import vid_cancion1
from Procedimientos.videofinalcancion2 import vid_cancion2
from Procedimientos.videofinalcancion3 import vid_cancion3
from Procedimientos.videopalabras import vid_videopalabras
from Procedimientos.transicionespecial import transicion_especial
from Procedimientos.mensajefinal import video_mensajefinal


def datos_sere_virtual(canciones, nombre, fraces, videocliente):
    canciones = canciones
    nombre = nombre
    fraces = fraces
    videocliente = videocliente
    estilo = ("EstilosVideos\estilo estandar.png")
    estilo_especial = ("EstilosVideos\Transicion especial.jpg")

    frase1 =  (f"{fraces[0]}")
    frase2 = (f"{fraces[1]}")
    frase3 = (f"{fraces[2]}")
    
    introin = ("EstilosVideos\Intro.mp4")
    transbasic = ("EstilosVideos\Transicion basica.mp4")
    intromotisere = ("Intro motivo serenata.mp4")
    cancion1 = (f"{canciones[0]}.mp4")   
    transespecial1 = (frase1) 
    cancion2 = (f"{canciones[1]}.mp4")
    transpalabras = ("Alguien quiere dedicarte unas palabras") 
    videopalabras = (videocliente)  
    transespecial2 = (frase2)
    cancion3 = (f"{canciones[2]}.mp4")
    transespecial3 = (frase3)
    mensafinal = ("EstilosVideos\Mensaje final.mp4")
    transdespedida = ("EstilosVideos\Transicion despedida.mp4")
    introout = ("EstilosVideos\Intro.mp4")
    
    v1 = introin
    v2 = transbasic              
    v3 = vid_intromotisere(intromotisere, nombre, estilo)
    v4 = vid_cancion1(cancion1, nombre, estilo)       
    v5 = transicion_especial(transespecial1, estilo_especial)
    v6 = vid_cancion2(cancion2, nombre, estilo)        
    v7 = transicion_especial(transpalabras, estilo_especial)           
    v8 = vid_videopalabras(videopalabras, nombre, estilo)                       
    v9 = transicion_especial (transespecial2, estilo_especial)            
    v10 = vid_cancion3(cancion3, nombre, estilo)          
    v11 = transicion_especial(transespecial3, estilo_especial)   
    v12 = video_mensajefinal(mensafinal, nombre, estilo)               
    v13 = transdespedida              
    v14 = introout
    

    list_clips = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, nombre]
   
    return list_clips

    
    
















   







