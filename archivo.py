#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import urllib.request
import matplotlib.pyplot as plt
import plotly.express as px
import folium
from streamlit_folium import st_folium
from PIL import Image

#URL del archivo en formato raw
#url ='https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciamiento%20Institucional_2.csv'
#Descargar y leer el archivo y considerar las comas como separadores
#datos = pd.read_csv(url, sep=',')
#st.line_chart(data=datos, x='NOMBRE', y='ESTADO_LICENCIAMIENTO')

#---------------------------------------------------------
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('upch.css') as f:
    st.markdown(f'<style>{f.read()}</upch>', unsafe_allow_html=True)
with st.sidebar: 
    st.markdown("###")
    st.sidebar.header('Programación Avanzada - Proyecto Final 2022-2')
    st.sidebar.info('Análisis y exploración de datos sobre el avance y estatus del Licenciamiento Institucional de las universidades peruanas.')
    selected = option_menu(
        menu_title = 'Menú',
        options = ['Inicio', 'Localización','Reportes','Equipo'],
        icons = ['house', 'map', 'book','people'],
        menu_icon='cast',
        default_index = 0,
        styles={
            "nav-link-selected":{"background-color":"skyblue"}
        },
    )
#--------------------------------------------------------- 
if selected == 'Inicio':
    st.markdown("<h1 style ='text-align: center'>SUNEDU:</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style ='text-align: center'>Licenciamiento Institucional</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader('Contexto:')
    st.write("En la actualidad, el principal reto que enfrenta la sociedad peruana en términos de educación superior es el de reorganizar el sistema universitario y promover uno basado en la calidad. Es así que en el 2014, la promulgación de la Ley Universitaria, Ley Nº 30220, introduce el licenciamiento obligatorio y renovable para las universidades tanto públicas como privadas del país con la finalidad de asegurar que se brinde un servicio educativo superior que cumpla con las Condiciones Básicas de Calidad (CBC) establecidas.")
    image = Image.open('Sunedu.jpg')
    st.image(image) 
    st.write("**Fuente**: Andina, 2021.")
    st.subheader('¿Qué es el Licenciamiento Institucional?')
    st.write("El Licenciamiento Institucional es un procedimiento obligatorio cuyo objetivo es verificar que las universidades cumplan con las CBC a fin de obtener una licencia que autorice su funcionamiento legal y, de esta manera, poder ofrecer un servicio educativo superior universitario. Como resultado, existe un sistema universitario más ordenado y con una mayor orientación hacia la mejora continua.")
    st.subheader('¿Qué son las Condiciones Básicas de Calidad?')
    st.write('Las Condiciones Básicas de Calidad (CBC) son un conjunto de estándares mínimos que constituyen un mecanismo de protección a los estudiantes, sus familias y la sociedad en conjunto, con los que una universidad debe contar para obtener el licenciamiento.')
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
        df_LI = pd.read_csv('Licenciamiento%20Institucional_2.csv')
        return df_LI
    download_data()
    st.dataframe(download_data())
    st.caption('Para mayor información acceder a: https://www.datosabiertos.gob.pe/dataset/sunedu-licenciamiento-institucional')
    #---------------------------------------------------------------------------------------------------------------------------
    st.header("Descripción del Dataset:")
    st.caption('A continuación, se proporciona una descripción de las variables incluidas en el Dataset.')
    @st.experimental_memo
    def download_data():
        url ="https://raw.githubusercontent.com/ximenarojo/prueba/main/variables.csv"
        filename ="variables.csv"
        urllib.request.urlretrieve(url,filename)
        df_variables = pd.read_csv('variables.csv')
        return df_variables
    download_data()
    st.dataframe(download_data())        
    
    st.markdown("###") 
    st.header('¡Comienza el análisis exploratorio!')
    st.write('**A continuación, seleccione una zona geográfica para visualizar el registro de universidades.**')
    st.markdown("###")
    df = pd.read_csv('Licenciamiento%20Institucional_2.csv')
    # Para minimizar el Dataset
    df = df.drop(columns =  ["CODIGO_ENTIDAD","NOMBRE","FECHA_INICIO_LICENCIAMIENTO","FECHA_FIN_LICENCIAMIENTO","LATITUD","LONGITUD","UBIGEO","FECHA_CORTE"])
    # -----------------------------------------------------
    set1 = np.sort(df['DEPARTAMENTO'].dropna().unique())
    sel1 = st.selectbox('Seleccione un departamento:', set1)
    df_DEPARTAMENTO = df[df['DEPARTAMENTO'] == sel1]
    n = len(df_DEPARTAMENTO.axes[0])
    # ----------------------------------------------------
    set2 = np.sort(df_DEPARTAMENTO['PROVINCIA'].dropna().unique())
    sel2 = st.selectbox('Seleccione una provincia:', set2)
    df_PROVINCIA = df_DEPARTAMENTO[df_DEPARTAMENTO['PROVINCIA'] == sel2]
    n = len(df_PROVINCIA.axes[0]) 
    # ---------------------------------------------------
    set3 = np.sort(df_DEPARTAMENTO['DISTRITO'].dropna().unique())
    sel3 = st.selectbox('Seleccione un distrito:', set3)
    df_DISTRITO = df_DEPARTAMENTO[df_DEPARTAMENTO['DISTRITO'] == sel3]
    n = len(df_DISTRITO.axes[0])
    st.write('Se encontraron', n,'registros de universidades para su búsqueda.')
    st.markdown("###") 
    
    st.markdown("###")
    pie_chart = df_DISTRITO.ESTADO_LICENCIAMIENTO.value_counts()
    pie_chart = pd.DataFrame(pie_chart)
    pie_chart = pie_chart.reset_index()
    pie_chart.columns = ['ESTADO_LICENCIAMIENTO','TOTAL']
    fig1, ax1 = plt.subplots()
    ax1.pie(pie_chart['TOTAL'], labels = pie_chart['ESTADO_LICENCIAMIENTO'], autopct='%1.1f%%')
    ax1.axis('equal')
    st.write('**Gráfico 1. Estado de Licenciamiento (en %) de las universidades según zona geográfica seleccionada.**')
    st.markdown("###")
    st.pyplot(fig1)
    
    st.markdown("###")
    bar_chart = df_DISTRITO.TIPO_GESTION.value_counts()
    bar_chart = pd.DataFrame(bar_chart)
    bar_chart.columns = ['Tipo de gestión']
    st.write('**Gráfico 2. Tipo de gestión de las universidades según zona geográfica seleccionada.**')
    st.markdown("###")
    st.bar_chart(bar_chart)
    
#--------------------------------------------------
df_otorgada = pd.read_csv('https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciadas.csv')
df_denegada = pd.read_csv('https://raw.githubusercontent.com/ximenarojo/prueba/main/no%20licenciadas.csv')
df_io = pd.read_csv('https://raw.githubusercontent.com/ximenarojo/prueba/main/io.csv')
df_ninguno = pd.read_csv('https://raw.githubusercontent.com/ximenarojo/prueba/main/Ninguno.csv')

if selected == 'Localización':
    st.markdown("<h1 style ='text-align: center'>Mapa interactivo: Localización</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write('**A continuación, seleccione una opción para visualizar la información.**')
    dataset = st.selectbox(
        'Seleccione una opción:',
        ('Licencia otorgada',
         'Licencia denegada',
         'Con informe de observaciones (IO) notificado',
         'Ninguno')
        )
    
    df_map = None
    opcion = '-'
    if dataset == 'Licencia otorgada':
        df_map = df_otorgada
        opcion = 'licencia otorgada'
        st.markdown("###")
        #st.write('**Gráfico 3. Universidades con '+opcion+' localizadas en un mapa interactivo mundial.**')
        
        
        map = folium.Map(
            location=[-9.19, -74], 
            zoom_start=5
        )
        Licenciada = pd.read_csv('Licenciadas.csv')
        Licenciada.head(5)
        Lic = Licenciada.loc[0]
        
        st_map = st_folium(map, width=800, height=450)
        
        
        
        st.markdown("###")
        st.write('**Lista de universidades con '+opcion+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_otorgada)
        n = len(df_otorgada.axes[0]) 
        
    elif dataset == 'Licencia denegada':
        df_map = df_denegada
        opcion = 'licencia denegada'
        st.markdown("###")
        st.write('**Lista de universidades con '+opcion+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_denegada)
        n = len(df_denegada.axes[0])
    elif dataset == 'Con informe de observaciones (IO) notificado':
        df_map = df_io
        opcion = 'informe de observaciones (IO) notificado'
        st.markdown("###")
        st.write('**Lista de universidades con '+opcion+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_io)
        n = len(df_io.axes[0])
        
    elif dataset == 'Ninguno':
        df_map = df_ninguno
        opcion = 'ningún estado de licenciamiento'
        st.markdown("###")
        st.write('**Lista de universidades con '+opcion+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_ninguno)
        n = len(df_ninguno.axes[0])
     
    
    st.write('Se encontraron', n,'registros de universidades para su búsqueda.')    
    
   
    
    
#--------------------------------------------------
if selected == 'Reportes':
    st.markdown("<h1 style ='text-align: center'>Períodos de Licenciamiento</h1>", unsafe_allow_html=True)
    st.markdown("---")

    
#--------------------------------------------------
if selected == 'Equipo':
    st.markdown("<h1 style='text-align: center'>¿Quiénes somos?</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write('Somos un grupo de estudiantes de 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia, que motivados por los conocimientos adquiridos por el curso de Programación Avanzada y junto a la asesoría de los profesores, hemos desarrollado una app interactiva para la visualización y exploración práctica de los datos recopilados sobre el avance y estatus actual del Licenciamiento Institucional de las Universidades tanto públicas como privadas del Perú.')
    st.markdown("###")
    image = Image.open('integrantes.jpg')
    st.image(image)
    st.markdown("###")
    st.header('Contáctanos:')
    contact_form = """
    <form action = "https://formsubmit.co/ximena.rojo@upch.pe" method="POST">
    <input type="hidden" name="_captcha" value="false" requiered>
    <input type="text" name="name" placeholder="Nombre" requiered>
    <input type="email" name="email" placeholder="Correo electrónico" requiered>
    <textarea name="message" placeholder="¡Escríbenos un mensaje!"></textarea>
    <button type= "submit">Enviar</button>
    </form>
    """ 
    st.markdown(contact_form, unsafe_allow_html=True)
    #Para dar formato:
    with open('message.css') as f:
        st.markdown(f'<style>{f.read()}</message>', unsafe_allow_html=True)
#---------------------------------------------------
