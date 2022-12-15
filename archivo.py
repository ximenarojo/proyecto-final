#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd 
import numpy as np  
from streamlit_option_menu import option_menu
import urllib.request
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts
from PIL import Image

#-------------------------------------------------------------------
#Insertamos la barra lateral
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('upch.css') as f:
    st.markdown(f'<style>{f.read()}</upch>', unsafe_allow_html=True) #Insertamos el logo upch
with st.sidebar: 
    st.markdown("###") #Lo utilizamos como un separador
    st.sidebar.header('Programación Avanzada - Proyecto Final 2022-2')
    st.sidebar.info('Análisis y exploración de datos sobre el avance y estatus del Licenciamiento Institucional de las universidades peruanas.')
    selected = option_menu(
        menu_title = 'Menú',
        options = ['Inicio', 'Localización','Periodo','Equipo'],   #Dividimos en secciones
        icons = ['house', 'map', 'book','people'],                 #Agregamos los iconos correspondientes a cada sección
        menu_icon='cast',
        default_index = 0,
        styles={
            "nav-link-selected":{"background-color":"skyblue"}     #Cambiamos el color de selección del menú a celeste
        },
    )

