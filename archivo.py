#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image


#---------------------------------------------------------
with st.sidebar:
    selected = option_menu(
        menu_title= 'Menú',
        options = ['Inicio', 'Reporte 2022', 'Nosotros'],
        icons=['house','book','people'],
        default_index=0,
    )
#--------------------------------------------------------- 
if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center'>SUNEDU:</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center'>Licenciamiento Institucional</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader('Contexto:')
    st.write("El mayor reto que enfrenta la sociedad peruana en materia de educación superior universitaria es el de reorganizar el sistema universitario y promover uno basado en la calidad. Es así que, La Ley Nº 30220, Ley Universitaria, entre otras medidas, creó la Superintendencia Nacional de Educación Superior Universitaria (SUNEDU) e introdujo la figura del licenciamiento obligatorio y renovable de las universidades. Gracias a esto, el Licenciamiento Institucional junto a la acreditación conforman dos etapas complementarias del aseguramiento de la calidad, que aseguran que se brinde un servicio educativo superior universitario en base a las Condiciones Básicas de Calidad (CBC) establecidas.")
    image= Image.open('Sunedu.jpg')
    st.image(image)
    st.write("**Fuente**: Andina, 2021.")
    st.subheader('¿Qué es el Licenciamiento Institucional?')
    st.write("El Licenciamiento Institucional es un requisito obligatorio para todas las universidades del país, a través del cual cada casa de estudios debe demostrar ante la SUNEDU que cumple con las Condiciones Básicas de Calidad (CBC) para poder brindar el servicio educativo. Como resultado de este proceso, existe un sistema universitario más ordenado y con una mayor orientación hacia la mejora continua.")
    st.subheader('¿Qué son las Condiciones Básicas de Calidad?')
    st.write('Las Condiciones Básicas de Calidad (CBC) son un conjunto de estándares mínimos con los que la universidad debe contar para obtener el licenciamiento. Estos constituyen un mecanismo de protección a los estudiantes, sus familias y a la sociedad en su conjunto.')
    image = Image.open('CBC.jpeg')
    st.image(image)
    st.write("**Fuente**: SUNEDU, 2018.")
    st.subheader('Etapas del Licenciamiento Institucional:')
    st.subheader("<h1 style='text-align: center; color: Blue '>Etapas del Licenciamiento Institucional:</h1>", unsafe_allow_html=True)
    video_file = open('Etapas del Licenciamiento para las universidades.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write('**Fuente**: SUNEDU, 2015.')
    st.markdown("---")
    st.subheader("Conoce la lista completa de las universidades licenciadas en el Perú:")
    
    
    

    #URL del archivo en formato raw
    url ='https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciamiento%20Institucional_2.csv'
    #Descargar y leer el archivo y considerar las comas como separadores
    datos = pd.read_csv(url, sep=',')
    st.line_chart(data=datos, x='NOMBRE', y='ESTADO_LICENCIAMIENTO')
  


    #st.markdown("---")
    st.caption("La información contenida en esta página web permite acceder al Dataset “Licenciamiento Institucional” elaborado por el Superintendencia Nacional de Educación Superior Universitaria (SUNEDU). Este ha registrado el avance y estatus del Licenciamiento Institucional de las universidades peruanas hasta el día 1 de septiembre de 2022.")
    st.caption("Fuente de datos: https://www.datosabiertos.gob.pe/dataset/sunedu-licenciamiento-institucional")

#--------------------------------------------------         
if selected == 'Nosotros':
             st.markdown("<h1 style='text-align: center; color: black;'>¿Quiénes somos?</h1>", unsafe_allow_html=True)
             st.markdown("---")
             st.write('Somos un grupo de estudiantes de 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia, que motivados por los conocimientos adquiridos por el curso de Programación Avanzada y junto a la asesoría de los profesores, hemos desarrollado un dashboard para el análisis, visualización y exploración práctica e interactiva de los datos recopilados sobre el avance y estatus actual del Licenciamiento Institucional de las Universidades tanto públicas como privadas del Perú.')
             st.markdown("##")
             image = Image.open('integrantes.jpg')
             st.image(image)
#---------------------------------------------------
