# _*_ coding: utf-8 _*_
import streamlit as st
from PIL import Image
from PIL import *
from numpy import *
from moviepy import *
import json
import os
import shutil
from Procedimientos.crearserenatavirtual import datos_sere_virtual
from Procedimientos.unir_serenata import union_clips_serenata
from Procedimientos.crearserenatavirtual import datos_sere_virtual


imalogo = Image.open("ima\logo.png")
st.set_page_config(page_title="Serenatas virtuales", page_icon=imalogo, layout="centered")


st.title("Serenata virtual")

#RUTAS A ARCHIVOS JSON
ruta_archivo_fraces = ("listfraces.json")
ruta_archivo_repertorio = ("listrepertorio.json")

#CARGA LA LISTA DE FRACES DEL ARCHIVO JSON LISTA DE FRACES
with open(ruta_archivo_fraces, "r", encoding="utf-8") as file:
     data = json.load(file)
     lista_fraces = data["lista_fraces"]

#CARGA EL MOTIVO Y REPERTORIO DE EL DICCIONARIO JSON REPERTORIO
with open(ruta_archivo_repertorio, "r", encoding="utf-8") as file:
     data = json.load(file)
     lista_motivo = data.keys()



def repertorio_selec(selec_motivo):
     with open(ruta_archivo_repertorio, "r", encoding="utf-8") as file:
          data = json.load(file)
          lista_canciones_motivo = data[selec_motivo]
     return lista_canciones_motivo


def clic_button_crear():
          if sel_motivo == "Selecciona un motivo":
               st.warning("Seleccione un motivo.")
          elif len(canciones_seleccionadas) != 3:
               st.warning("Seleccione las 3 canciones.")
          elif nombre_homenajeado == "":
               st.warning("ingrese el nombre de la persona homenajeada.")
          elif len(fraces_intro_seleccion) != 3:
               st.warning("Selecciona las 3 fraces.")
          elif video_palabras_cliente == None:
               st.warning("Sube el video de 1 minuto con tu saludo.")
          else:
               return True

def guardar_archivo(uploadedfile):
         # CREAR DIRECTORIO SI NO EXISTE
         if not os.path.exists("tempcli"):
              os.makedirs("tempcli")

         # GUARDAR EL ARCHIVO EN EL DIRECTORIO
         with open(os.path.join("tempcli", uploadedfile.name), "wb") as f:
              f.write(uploadedfile.getbuffer())

         return (uploadedfile.name)

def vaciar_carpeta(ruta_carpeta):
      if os.path.exists(ruta_carpeta) and os.path.isdir(ruta_carpeta):
            for nombre_archivo in os.listdir(ruta_carpeta):
                 ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
                 try:
                       if os.path.isfile(ruta_completa) or os.path.islink(ruta_completa):
                         os.unlink(ruta_completa)   

                       elif os.path.isdir(ruta_completa):
                             shutil.rmtree(ruta_completa)
                 except Exception as e:
                       st.warning(body=f"Error al eliminar {ruta_completa}. Razon {e}")             
      else:
            st.warning(f"La carpeta {ruta_carpeta} no existe o no es una carpeta.")

                     
sel_motivo = st.selectbox(label="Selecciona el motivo de la serenata.", options=lista_motivo, placeholder="Seleccionar motivo", key="sel_moti_key")
reper_motivo_selec = repertorio_selec(sel_motivo)

canciones_seleccionadas = st.multiselect(label="Selecciona 3 canciones.", key="can_sel", placeholder="Seleccionar canciones", options=reper_motivo_selec, max_selections=3)

nombre_homenajeado = st.text_input(label="Nombre de la persona homenajeada.", key="nom_hom", value="")

fraces_intro_seleccion = st.multiselect(label="Selecciona 3 fraces.", key="fra_int_sel", placeholder="Seleccionar fraces", options=lista_fraces, max_selections=3)
    
video_palabras_cliente = st.file_uploader(label="Sube un video de maximo 1 minuto de 1280x720px a 30fps.", key="vid_cli", help="", type="mp4", accept_multiple_files=False)


if video_palabras_cliente is not None: 
     video_palabras_cliente_ruta = guardar_archivo(video_palabras_cliente)  
     estado = clic_button_crear()

     if estado is True:

          clic_button = st.button(label="Crear serenata virtual", use_container_width=True) 

          if clic_button is True: 

               with st.spinner(text="Creando tu serenata virtual...", show_time=True): 
                    lista_videos = datos_sere_virtual(canciones_seleccionadas, nombre_homenajeado, fraces_intro_seleccion, video_palabras_cliente_ruta) 
                    video_final = union_clips_serenata(lista_videos)
               
                    if video_final is not None:
                               
                               ruta_carpeta_temp = "temp"
                               ruta_carpeta_tempcli = "tempcli"
                               
                               vaciar_carpeta(ruta_carpeta=ruta_carpeta_temp)
                               vaciar_carpeta(ruta_carpeta=ruta_carpeta_tempcli)

                               ruta_archivo = "listserevir.json"
                               lista_serenatas = {"Lista": [video_final]}

                               if not os.path.exists(ruta_archivo):
                                     with open(ruta_archivo, "w") as file:
                                           json.dump(lista_serenatas, file, indent=4, ensure_ascii=False)
                                           st.switch_page("app.py")
                               else:
                                     with open(ruta_archivo, "r") as file:
                                           data = json.load(file)
                                           if "Lista" in data and isinstance(data["Lista"], list):
                                                 data["Lista"].append(video_final)
                                                 with open(ruta_archivo, "w") as file:
                                                       json.dump(data, file, indent=4, ensure_ascii=False)
                                                       st.switch_page("app.py")
                         



 








      
      

  

        
        
        
    
                 














     
                                         

    
#datos_sere_virtual(canciones_seleccionadas, nombre_homenajeado, fraces_intro_seleccion, video_palabras_cliente)











        

    
    




