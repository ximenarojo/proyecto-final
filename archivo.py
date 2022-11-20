#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image
import gdown
import os


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
    st.header('¿Qué es el Licenciamiento Institucional?')
    st.write("El Licenciamiento Institucional es un requisito obligatorio para todas las universidades del país, a través del cual cada casa de estudios debe demostrar ante la Superintendencia Nacional de Educación Superior Universitaria (SUNEDU) que cumple con las Condiciones Básicas de Calidad (CBC) para poder brindar el servicio educativo. Como resultado de este proceso, existe un sistema universitario más ordenado y con una mayor orientación hacia la mejora continua (SUNEDU, 2018).")
    st.markdown("##")
    st.header('Condiciones Básicas de Calidad (CBC)')
    st.write('Las Condiciones Básicas de Calidad (CBC) son un conjunto de estándares mínimos con los que la universidad debe contar para obtener el licenciamiento. Estos constituyen un mecanismo de protección a los estudiantes, sus familias y a la sociedad en su conjunto (SUNEDU, 2018).')
    image = Image.open('CBC.jpeg')
    st.image(image)
    st.write("**Fuente**: SUNEDU (2018). Disponible en: https://www.sunedu.gob.pe/8-condiciones-basicas-de-calidad/")
    st.markdown("##")
    st.header('¿Cuáles son las etapas del Licenciamiento Institucional?')
    video_file = open('Etapas del Licenciamiento para las universidades.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write('**Fuente**: SUNEDU, 2015.')
    st.markdown("---")
    st.header("Conoce la lista completa de las universidades licenciadas en el Perú:")
    st.header("Tabla de datos:")
    
    

    #URL del archivo en formato raw
    url ='https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciamiento%20Institucional_2.csv'
    #Descargar y leer el archivo y considerar las comas como separadores
    datos = pd.read_csv(url, sep=',')
    st.line_chart(data=datos, x='NOMBRE', y='ESTADO_LICENCIAMIENTO')
    
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    @st.experimental_memo
    def download_data():
        #https://drive.google.com/uc?id=
        url = "https://drive.google.com/uc?id=13yU9xnaFk0nyFV4O5uePmD1aaruFdCoq"
        output = "downloads/data.csv"
        gdown.download(url,output,quiet = False)
    
    download_data()
    df = pd.read_csv("downloads/data.csv", sep = ";", parse_dates = ["FECHA_CORTE","FECHA_RESULTADO"])
    #Simplificacion del dataset (retiro de columnas)
    df = df.drop(columns = ["FECHA_CORTE","FECHA_RESULTADO","UBIGEO","id_persona"])
    
    #Sistema de filtros
    #Construccion del set/list de departamentos (Valores unicos sin NA)
    set_departamentos = np.sort(df['DEPARTAMENTO'].dropna().unique())
    #Seleccion del departamento
    opcion_departamento = st.selectbox('Selecciona un departamento', set_departamentos)
    df_departamentos = df[df['DEPARTAMENTO'] == opcion_departamento]
    num_filas = len(df_departamentos.axes[0]) 
    #Construccion del set/list de provincias (Valores unicos sin NA)
    set_provincias = np.sort(df_departamentos['PROVINCIA'].dropna().unique())#Seleccion de la provincia
    opcion_provincia = st.selectbox('Selecciona una provincia', set_provincias)
    df_provincias = df_departamentos[df_departamentos['PROVINCIA'] == opcion_provincia]
    num_filas = len(df_provincias.axes[0]) 
    
    st.write('Numero de registros:', num_filas)
   

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
