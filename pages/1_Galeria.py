import streamlit as st
from PIL import Image
import json
import os



imalogo = Image.open("ima\logo.png")
st.set_page_config(page_title="Galeria", page_icon=imalogo, layout="centered")


###blue green orange red violet ###
ruta_archivo = "listserevir.json"


def eliminar_valor(i):
        with open(ruta_archivo, "r") as file:
            data = json.load(file)
            if i in data["Lista"]:
                data["Lista"].remove(i)
                with open(ruta_archivo, "w") as file:
                    json.dump(data, file, indent=4)
                    os.remove(i)
                    
                
            
@st.dialog(title=" ", width="small")
def abri_dialogo(n, v):
    titulo_eti = n
    video_eti = v
    st.text(titulo_eti)
    st.video(data=video_eti, format="video/mp4")

    
     
st.title("Galeria")
    

with open(ruta_archivo, "r") as file:
    data = json.load(file)
    if data["Lista"] == []:
        st.text("No hay serenatas.")     
    else:
        with open(ruta_archivo, "r") as file:
            data = json.load(file)
            lista = data["Lista"]
            lista.reverse()
            for i in lista:          
                nombre = i
                sintemp = nombre.replace("Video final", "")
                sinbarra = sintemp[1:]
                col1, col2 = st.columns([5, 1])
                with col1:
                    st.button(label=f"Ver {sinbarra}", type="secondary", use_container_width=True, on_click=abri_dialogo, args=[sinbarra, i])
                with col2:
                    btn_eliminar_video = st.button(label="Eliminar ", type="tertiary", key=f"{sinbarra}", use_container_width=True, on_click=eliminar_valor, args=(i,))
                    if btn_eliminar_video:
                        eliminar_valor(i)

                st.divider() 