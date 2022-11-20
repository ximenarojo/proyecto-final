#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image
import urllib.request

#---------------------------------------------------------
with st.sidebar:
    selected = option_menu(
        menu_title= 'Menú',
        options = ['Inicio', 'Nosotros'],
        icons=['house', 'people'],
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
    video_file = open('Etapas del Licenciamiento para las universidades.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write('**Fuente**: SUNEDU, 2015.')
    st.markdown("---")
    st.header("Estatus del Licenciamiento Institucional:")
    st.caption('La información presentada a continuación permite acceder al Dataset “Licenciamiento Institucional” elaborado por la Superintendencia Nacional de Educación Superior Universitaria (SUNEDU) donde se ha registrado el avance y estatus del Licenciamiento Institucional de las universidades del Perú.')
    st.caption ('Última actualización: 31/08/2022.')
    @st.experimental_memo
    def download_data():
        url ="https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciamiento%20Institucional_2.csv"
        filename ="Licenciamiento%20Institucional_2.csv"
        urllib.request.urlretrieve(url,filename)
        df =pd.read_csv('Licenciamiento%20Institucional_2.csv')
        return df
    download_data()
    st.dataframe(download_data())
    st.caption('Para mayor información acceder a: https://www.datosabiertos.gob.pe/dataset/sunedu-licenciamiento-institucional')
    st.markdown("###")
    st.subheader('Análisis exploratorio')
    st.write('Para visualizar la información de una zona geográfica específica del Perú, seleccione el nombre de un departamento, provincia y distrito.')
    
    df =pd.read_csv('Licenciamiento%20Institucional_2.csv')
    #Simplificar el Dataset
    df = df.drop(columns = ["CODIGO_ENTIDAD","NOMBRE","TIPO_GESTION","FECHA_INICIO_LICENCIAMIENTO","FECHA_FIN_LICENCIAMIENTO","UBIGEO","LATITUD","LONGITUD", "FECHA_CORTE"])
    set_dep = np.sort(df['DEPARTAMENTO'].dropna().unique())
    op_dep = st.selectbox('Por favor, seleccione un departamento', set_dep)
    df_dep = df[df['DEPARTAMENTO'] == op_dep]
    num_filas = len(df_dep.axes[0])
    
    set_prov = np.sort(df_dep['PROVINCIA'].dropna().unique())
    op_prov = st.selectbox('Por favor, seleccione una provincia', set_prov)
    df_prov = df_dep[df_dep['PROVINCIA'] == op_prov]
    num_filas = len(df_prov.axes[0]) 

    set_dist = np.sort(df_dep['DISTRITO'].dropna().unique())
    op_dist = st.selectbox('Por favor, seleccione un distrito', set_dist)
    df_dist = df_dep[df_dep['DISTRITO'] == op_dist]
    num_filas = len(df_dist.axes[0]) 
    
    st.write('Numero de registros:', num_filas)
    
    
    
#-------------------------------------------------- 

    #URL del archivo en formato raw
    #url ='https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciamiento%20Institucional_2.csv'
    #Descargar y leer el archivo y considerar las comas como separadores
    #datos = pd.read_csv(url, sep=',')
    #st.line_chart(data=datos, x='NOMBRE', y='ESTADO_LICENCIAMIENTO')

#-------------------------------------------------- 
if selected == 'Nosotros':
             st.markdown("<h1 style='text-align: center; color: black;'>¿Quiénes somos?</h1>", unsafe_allow_html=True)
             st.markdown("---")
             st.write('Somos un grupo de estudiantes de 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia, que motivados por los conocimientos adquiridos por el curso de Programación Avanzada y junto a la asesoría de los profesores, hemos desarrollado un dashboard para el análisis, visualización y exploración práctica e interactiva de los datos recopilados sobre el avance y estatus actual del Licenciamiento Institucional de las Universidades tanto públicas como privadas del Perú.')
             st.markdown("###")
             image = Image.open('integrantes.jpg')
             st.image(image)
#---------------------------------------------------

