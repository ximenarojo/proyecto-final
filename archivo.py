#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
    
st.markdown("<h1 style='text-align: center; color: black;'>SUNEDU:</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Licenciamiento Institucional</h1>", unsafe_allow_html=True)
st.markdown("---")
st.header('¿Quiénes somos?')
st.caption('Somos un grupo de estudiantes del 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia, que motivados por los conocimientos adquiridos por el curso de Programación Avanzada y junto a la asesoría de los profesores, hemos desarrollado un dashboard para el análisis, visualización y exploración práctica e interactiva de los datos recopilados sobre el avance y estatus actual del Licenciamiento Institucional de las Universidades tanto públicas como privadas del Perú.')
image = Image.open('integrantes.jpg')
st.image(image)
st.markdown("---")
st.header('¿Qué es el Licenciamiento Institucional?')
st.write("El Licenciamiento Institucional es un requisito obligatorio para todas las universidades del país, a través del cual cada casa de estudios debe demostrar ante la Superintendencia Nacional de Educación Superior Universitaria (SUNEDU) que cumple con las Condiciones Básicas de Calidad (CBC) para poder brindar el servicio educativo. Como resultado de este proceso, existe un sistema universitario más ordenado y con una mayor orientación hacia la mejora continua (SUNEDU,2018).")

st.markdown("##")
st.header('Condiciones Básicas de Calidad (CBC)')
st.write("Las Condiciones Básicas de Calidad (CBC) son un conjunto de estándares mínimos con los que la universidad debe contar para obtener el licenciamiento. Estos constituyen un mecanismo de protección a los estudiantes, sus familias y a la sociedad en su conjunto (SUNEDU, 2018).")
image = Image.open('CBC.jpeg')
st.image(image, caption="Imagen tomada de SUNEDU(2018). Disponible en: https://www.sunedu.gob.pe/8-condiciones-basicas-de-calidad/")
st.markdown("##")
st.header('¿Por qué es importante contar con Licenciamiento Institucional?')
st.write("")
