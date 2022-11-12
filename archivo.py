#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
"""
#------------------------------------------------------------------------------------------------------------
# Bibliotecas
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
from PIL import Image

#------------------------------------------------------------------------------------------------------------
st.markdown("<h1 style='text-align: center; color: black;'>SUNEDU: Licenciamiento Institucional</h1>", unsafe_allow_html=True)
st.markdown("##")

st.markdown("<h1 style='text-align: center; color: black;'>Programación Avanzada - Proyecto 2022-2</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("##")

st.header('¿Quiénes somos?')
st.markdown("##")
st.caption('Somos un grupo de estudiantes de 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia ...')
st.markdown("##")

image = Image.open('borrador(1).jpg')
st.markdown("##") # Linea en blanco
