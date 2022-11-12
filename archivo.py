#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.markdown("<h1 style='text-align: center; color: black;'>SUNEDU: Licenciamiento Institucional</h1>", unsafe_allow_html=True)
st.markdown("##")
st.markdown("<h1 style='text-align: left; size: 12; color: black;'>Programación Avanzada - Proyecto 2022-2</h1>", unsafe_allow_html=True)
st.markdown("---")
st.header('¿Quiénes somos?')
st.caption('Somos un grupo de estudiantes del 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia, que motivados por los conocimientos adquiridos por el curso de Programación Avanzada y junto a la asesoría de los profesores, hemos creado un dashboard para el análisis, visualización y exploración práctica e interactiva de los datos recopilados sobre el avance y estatus actual del Licenciamiento Institucional de las Universidades tanto públicas como privadas del Perú.')
image = Image.open('integrantes.jpg')
st.image(image)

