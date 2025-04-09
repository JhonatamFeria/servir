# _*_ coding: utf-8 _*_
import streamlit as st
from PIL import Image
import os 
import json




st.set_page_config(page_title="Configuracion", layout="centered")


#CONFIGURACIONES DE LA APP
st.title("Configuracion")


#RUTAS DE LA APP

ruta_archivo = "listmotivo.json"


#FUNCIONE DE ALERTA DE FORMULARIO
def alerta(text_alert):
    st.warning(text_alert)

#FUNCION DE PROCESO EXITOSO
def exitoso(n, e):
    st.success(f"{n} {e} exitosamente")





#FUNCION DE GUARDAR NUEVA CANCION EN CARPETA VIDEOS
def guardar_archivo_nuevid(uploadedfile):
         # CREAR DIRECTORIO SI NO EXISTE
         if not os.path.exists("CancionesVideos"):
              os.makedirs("CancionesVideos")

         # GUARDAR EL ARCHIVO EN EL DIRECTORIO
         with open(os.path.join("CancionesVideos", uploadedfile.name), "wb") as f:
              f.write(uploadedfile.getbuffer())

         return (uploadedfile.name)

#FUNCION DE GUARDAR NUEVA INTRO O TRNASICION EN LA CARPETA VIDEOS
def guardar_archivo_introotrans(uploadedfile):
         # CREAR DIRECTORIO SI NO EXISTE
         if not os.path.exists("Videos"):
              os.makedirs("Videos")

         # GUARDAR EL ARCHIVO EN EL DIRECTORIO
         with open(os.path.join("Videos", uploadedfile.name), "wb") as f:
              f.write(uploadedfile.getbuffer())

         return (uploadedfile.name)



#CONFIGURACION MOTIVO
with st.expander(label="Editar lista motivo"):
    input_motivo = st.text_input(label="Motivo")
    col1, col2 = st.columns(2)
    with col1:
        btn_guar_moti = st.button(label="Guardar", use_container_width=True, key="btn_guar_moti")
        if btn_guar_moti:
            if input_motivo == "":
                alerta("Ingrese un motivo nuevo")
            else:
                ruta_archivo = "listmotivo.json"
                lista_motivo = {"Lista": [input_motivo]}
                
                if not os.path.exists(ruta_archivo):
                      with open(ruta_archivo, "w", encoding="utf-8") as file:
                        json.dump(lista_motivo, file, indent=4, ensure_ascii=False)
                        file.close
                else:
                    with open(ruta_archivo, "r", encoding="utf-8") as file:
                        data = json.load(file)
                        if "Lista" in data and isinstance(data["Lista"], list):
                            data["Lista"].append(input_motivo)
                            with open(ruta_archivo, "w") as file:
                                json.dump(data, file, indent=4, ensure_ascii=False)  
        
    with col2:
        btn_elim_moti = st.button("Eliminar", use_container_width=True, key="btn_elim_moti")
        if btn_elim_moti:
            if input_motivo == "":
                st.warning("Ingrese el motivo a eliminar.")
            else:
                ruta_archivo = "listmotivo.json"
                lista_motivo = {"Lista": [input_motivo]}
                
                if not os.path.exists(ruta_archivo):
                      with open(ruta_archivo, "w", encoding="utf-8") as file:
                        json.dump(lista_motivo, file, indent=4, ensure_ascii=False)
                        file.close
                else:
                    with open(ruta_archivo, "r") as file:
                        data = json.load(file)
                        if "Lista" in data and isinstance(data["Lista"], list):
                            data["Lista"].remove(input_motivo)
                            with open(ruta_archivo, "w", encoding="utf-8") as file:
                                json.dump(data, file, indent=4, ensure_ascii=False)
    
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        data = json.load(file)
        list = (data["Lista"])
        st.write(list)


#CONFIGURACION REPERTORIO
with st.expander(label="Editar repertorio"):
    ruta_archivo_repertorio = "listrepertorio.json"
    with open(ruta_archivo_repertorio, "r", encoding="utf-8") as file:
        diccionario = json.load(file)  
        llaves = diccionario.keys()
        
        llave_seleccionada = st.selectbox(label="Seleccione el motivo", options=llaves)
        
        input_cancion = st.text_input(label="Ingresa la cancion a eliminar")
       
        nuevo_video = st.file_uploader(label="Selecciona el video a guardar.", key="", help="video recomendado: .mp4 1280x720px a 30fps", type="mp4", accept_multiple_files=False) 
        if nuevo_video != None:
            nuevo_video_nombre = nuevo_video.name
            nuevidnom = nuevo_video_nombre.replace(".mp4", "")

        col1, col2 = st.columns(2)

        with col1:
            
            btn_guar_can = st.button(label="Guardar", use_container_width=True, key="btn_guar_can")
            if btn_guar_can:
                if nuevo_video == None:
                            st.warning("Seleccione un video nuevo")
                else:
                    with open(ruta_archivo_repertorio, "r", encoding="utf-8") as file:
                        data = json.load(file)
                        data[llave_seleccionada].append(nuevidnom)
                        with open(ruta_archivo_repertorio, "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                            guardar_archivo_nuevid(nuevo_video)
                            exitoso(input_cancion, " se guardo ")

        with col2:
            
            btn_elim_can = st.button(label="Eliminar", use_container_width=True, key="btn_elim_can")
            if btn_elim_can:
                if input_cancion == "":
                    alerta("Ingrese la cancion a eliminar")
                else:
                    with open(ruta_archivo_repertorio, "r", encoding="utf-8") as file:
                        data = json.load(file)
                        data[llave_seleccionada].remove(input_cancion)
                        with open(ruta_archivo_repertorio, "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                            os.remove(f"CancionesVideos\{input_cancion}.mp4")
                            exitoso(input_cancion, " se elimino ")
                        
    st.write(diccionario[llave_seleccionada])
        

#CONFIGURACION FRACES                                         
with st.expander(label="Editar frases"):
    ruta_archivo_fraces = "listfraces.json"
    input_frace = st.text_input("Ingresa la frace")

    col1, col2 = st.columns(2)

    with col1:
        btn_guardar_frace = st.button(label="Gardar", use_container_width=True, key="btn_guardar_frace")
        if btn_guardar_frace:
            with open(ruta_archivo_fraces, "r", encoding="utf-8") as file:
                data = json.load(file)
                data["lista_fraces"].append(input_frace)
                with open(ruta_archivo_fraces, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
    
    with col2:
        btn_eliminar_frace = st.button(label="Eliminar", use_container_width=True, key="btn_eliminar_frace")
        if btn_eliminar_frace:
            with open(ruta_archivo_fraces, "r", encoding="utf-8") as file:
                data = json.load(file)
                data["lista_fraces"].remove(input_frace)
                with open(ruta_archivo_fraces, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)

    with open(ruta_archivo_fraces, "r", encoding="utf-8") as file:
        data = json.load(file)
        lista_fraces = data["lista_fraces"]
        st.write(lista_fraces)
   

#CONFIGURACION INTRO Y TRANSICIONES
with st.expander(label="Editar intro y trancisiones"):
    st.text("Se requieren los sigueintes videos para su funcionamiento:\nIntro.mp4, Transicion Basica.mp4, Intro motivo serenata.mp4, Canciones.mp4, Frases.mp4, Transicion Palabras.mp4, Mensaje final.mp4, Transicion Despedida.mp4")
    eliminar_introotrans = st.text_input(label="Ingresa la intro o transicion a eliminar")
    nueva_introytrans = st.file_uploader(label="Seleccionar nueva intro o transicion")

    col1, col2 = st.columns(2)

    with col1:
        btn_guardar_introotrans = st.button(label="Guardar", use_container_width=True)
        if btn_guardar_introotrans:
            if nueva_introytrans is None:
                alerta("Seleccione una intro o trnasicion")
            else:
                guardar_archivo_introotrans(nueva_introytrans)
                exitoso(nueva_introytrans.name, " se guardo ")

    with col2:
        btn_eliminar_introotrans = st.button(label="Elimiar", use_container_width=True) 
        if btn_eliminar_introotrans:
            if eliminar_introotrans == "":
                alerta("Ingrese la cancion a eliminar")  
            else:
                os.remove(f"Videos\{eliminar_introotrans}")
                exitoso(eliminar_introotrans, " se elimino ")


    #especifica la ruta de la carpeta
    ruta_carpeta_videos = "EstilosVideos"
    #obtiene la lista de archivos y directorios en la carpeta
    nombres_archivos = os.listdir(ruta_carpeta_videos)
    #filtra solo los archivos (excluye directorios)
    archivos = [nombre for nombre in nombres_archivos if os.path.isfile(os.path.join(ruta_carpeta_videos, nombre))]
    st.write(archivos)
    


            
              
        
    
    


    
