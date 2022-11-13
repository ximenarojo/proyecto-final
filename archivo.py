#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import gdown
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
st.subheader("¿Qué es la SUNEDU?") 
col1, col2 = st.columns(2)
with col1:
     st.write("La Superintendencia Nacional de Educación Superior Universitaria (SUNEDU) es un organismo peruano adscrito al Ministerio de Educación con autonomía técnica, funcional, administrativa, económica y financiera, el cual se encarga de administrar el Registro Nacional de Grados y Títulos, bajo la consigna de brindar seguridad jurídica de la información que se encuentra registrada y garantizar su autenticidad. Asimismo, tiene como finalidad el licenciamiento, supervisión de la calidad, fiscalización del servicio educativo superior universitario.")
with col2:
    image= Image.open('SUNEDU.jpg')
    st.image(image)
st.markdown("##")
st.header('Condiciones Básicas de Calidad (CBC)')
st.write("Las Condiciones Básicas de Calidad (CBC) son un conjunto de estándares mínimos con los que la universidad debe contar para obtener el licenciamiento. Estos constituyen un mecanismo de protección a los estudiantes, sus familias y a la sociedad en su conjunto (SUNEDU, 2018).")
image = Image.open('CBC.jpeg')
st.image(image)
st.write("**Fuente**: SUNEDU (2018). Disponible en: https://www.sunedu.gob.pe/8-condiciones-basicas-de-calidad/")
st.markdown("##")
st.header('Etapas del Licenciamiento para universidades')
video_file = open('Etapas del Licenciamiento para las universidades.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("**Fuente**: SUNEDU. (2015). https://youtu.be/2NlkqlD7RTE&t=26s")   
st.markdown("---")
st.header("Conoce la lista completa de las universidades licenciadas en el Perú a la fecha (2022-09-01):")

st.markdown("""
Por favor, seleccione un departamento, provincia y distrito para visualizar las universidades licenciadas correspondientes a una zona geográfica específica del Perú. 
""")
#id = 12x_Bum-PL4dXjQbdGTKji7EKUTdfq_7v
if not os.path.exists('downloads'):
  os.makedirs('downloads')

@st.experimental_memo
def download_data():
    #https://drive.google.com/uc?id=
    url = "https://drive.google.com/uc?id=12x_Bum-PL4dXjQbdGTKji7EKUTdfq_7v"
    output = "downloads/data.csv"
    gdown.download(url,output,quiet = False)
 
download_data()
df = pd.read_csv("downloads/data.csv", sep = ";", parse_dates = ["FECHA_CORTE","FECHA_RESULTADO"])
#Retiro de columnas
df = df.drop(columns = ["CODIGO_ENTIDAD", "NOMBRE", "TIPO_GESTION", "ESTADO_LICENCIAMIENTO","FECHA_INICIO_LICENCIAMIENTO","FECHA_FIN_LICENCIAMIENTO","PERIODO_LICENCIAMIENTO", "UBIGEO","LATITUD", "LONGITUD", "FECHA_CORTE"]

set_dep = np.sort(df['DEPARTAMENTO'].dropna().unique())
op_dep = st.selectbox('Selecciona un departamento', set_dep)
df_dep = df[df['DEPARTAMENTO'] == op_dep]
filas = len(df_dep.axes[0]) 

set_prov = np.sort(df_dep['PROVINCIA'].dropna().unique())
op_prov = st.selectbox('Selecciona una provincia', set_prov)
df_prov = df_dep[df_dep['PROVINCIA'] == op_prov]
filas = len(df_prov.axes[0]) 

set_dist = np.sort(df_dep['DISTRITO'].dropna().unique())
op_dist = st.selectbox('Selecciona un distrito', set_dist)
df_dist = df_dep[df_dep['DISTRITO'] == op_dist]
filas = len(df_dist.axes[0]) 
             
st.write('Número de registros:', filas)

