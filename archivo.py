#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.markdown("<h1 style='text-align: center; color: black;'>SUNEDU: Licenciamiento Institucional</h1>", unsafe_allow_html=True)
st.markdown("##")
st.markdown("<h1 style='text-align: center; color: black;'>Programación Avanzada - Proyecto 2022-2</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("##")
st.header('¿Quiénes somos?')
st.caption('Somos un grupo de estudiantes de 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia, que motivados por el curso de Programación Avanzada hemos creado ..')
st.markdown("##")
image = Image.open('integrantes.jpg')
