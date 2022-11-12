#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.markdown("<h1 style='text-align: center; color: black;'>SUNEDU: Licenciamiento Institucional</h1>", unsafe_allow_html=True)
st.markdown("##")

st.markdown("<h1 style='text-align: center; color: black;'>Programación Avanzada - Proyecto 2022-2</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("##")

st.header('¿Quiénes somos?')
st.markdown("##")
st.caption('Somos un grupo de estudiantes de 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia ...')
st.markdown("##")

from PIL import Image
image = Image.open('borrador(1).jpg')
