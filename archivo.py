#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd 
import numpy as np
from streamlit_option_menu import option_menu
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image

#-----------------------------------------------------------
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('upch.css') as f:
    st.markdown(f'<style>{f.read()}</upch>', unsafe_allow_html=True)
with st.sidebar: 
    st.markdown("###")
    st.sidebar.header('Programación Avanzada - Proyecto Final 2022-2')
    st.sidebar.info('Análisis y exploración de datos sobre el avance y estatus del Licenciamiento Institucional de las universidades peruanas.')
    selected = option_menu(
        menu_title = 'Menú',
        options = ['Inicio', 'Localización','Funcionamiento','Equipo'],
        icons = ['house', 'map', 'book','people'],
        menu_icon='cast',
        default_index = 0,
        styles={
            "nav-link-selected":{"background-color":"skyblue"}
        },
    )
#------------------------------------------------------------------------------------------------------------
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
    st.write('Las Condiciones Básicas de Calidad (CBC) son estándares mínimos que sirven de pautas generales para la evaluación de la capacidad de la universidad para la prestación del servicio educativo superior universitario y autorización de su funcionamiento.')
    image = Image.open('CBC.jpeg')
    st.image(image)
    st.write("**Fuente**: SUNEDU, 2018.")
    st.subheader('Etapas del Licenciamiento Institucional:')
    image = Image.open('Etapas.jpeg')
    st.image(image)
    video_file = open('Etapas del Licenciamiento para las universidades.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write('**Fuente**: SUNEDU, 2016.')
    st.markdown("---")
    st.header("Estatus del Licenciamiento Institucional:")
    st.caption('La información presentada a continuación permite acceder al Dataset “Licenciamiento Institucional” elaborado por la Superintendencia Nacional de Educación Superior Universitaria (SUNEDU) donde se ha registrado el avance y estatus del Licenciamiento Institucional de las universidades del Perú.')
    st.caption ('Última actualización: 31/08/2022.')
    
    @st.experimental_memo
    def download_data():
        url ="https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciamiento%20Institucional_2.csv"
        filename ="Licenciamiento%20Institucional_2.csv"
        urllib.request.urlretrieve(url,filename)
        df = pd.read_csv('Licenciamiento%20Institucional_2.csv')
        return df
    download_data()
    st.dataframe(download_data())
    st.caption('Para mayor información acceder a: https://www.datosabiertos.gob.pe/dataset/sunedu-licenciamiento-institucional')
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
    st.write('**Gráfico 1. Registro (en general) de la cantidad de universidades existentes por departamento.**')
    df = pd.read_csv('Licenciamiento%20Institucional_2.csv')
    df_dep = pd.DataFrame(df["DEPARTAMENTO"].value_counts())
    st.bar_chart(df_dep)
    
    st.write('**A continuación, seleccione una zona geográfica para visualizar el registro de universidades.**')
    st.markdown("###")
    df = pd.read_csv('Licenciamiento%20Institucional_2.csv')
    df = df.drop(columns = ["CODIGO_ENTIDAD","NOMBRE","FECHA_INICIO_LICENCIAMIENTO","FECHA_FIN_LICENCIAMIENTO","LATITUD","LONGITUD","UBIGEO","FECHA_CORTE"])
    
    set1 = np.sort(df['DEPARTAMENTO'].dropna().unique())
    sel1 = st.selectbox('Seleccione un departamento:', set1)
    df_DEPARTAMENTO = df[df['DEPARTAMENTO'] == sel1]
    n = len(df_DEPARTAMENTO.axes[0])
    
    set2 = np.sort(df_DEPARTAMENTO['PROVINCIA'].dropna().unique())
    sel2 = st.selectbox('Seleccione una provincia:', set2)
    df_PROVINCIA = df_DEPARTAMENTO[df_DEPARTAMENTO['PROVINCIA'] == sel2]
    n = len(df_PROVINCIA.axes[0]) 
    
    set3 = np.sort(df_DEPARTAMENTO['DISTRITO'].dropna().unique())
    sel3 = st.selectbox('Seleccione un distrito:', set3)
    df_DISTRITO = df_DEPARTAMENTO[df_DEPARTAMENTO['DISTRITO'] == sel3]
    n = len(df_DISTRITO.axes[0])
    st.write('Se encontraron', n,'registros de universidades para su búsqueda.')
    
    st.markdown("###")
    pie_chart = df_DISTRITO.ESTADO_LICENCIAMIENTO.value_counts()
    pie_chart = pd.DataFrame(pie_chart)
    pie_chart = pie_chart.reset_index()
    pie_chart.columns = ['ESTADO_LICENCIAMIENTO','TOTAL']
    fig1, ax1 = plt.subplots()
    ax1.pie(pie_chart['TOTAL'], labels = pie_chart['ESTADO_LICENCIAMIENTO'], autopct='%1.1f%%')
    ax1.axis('equal')
    st.write('**Gráfico 2. Estado de Licenciamiento (en %) de las universidades según zona geográfica seleccionada.**')
    st.markdown("###")
    st.pyplot(fig1)

    st.markdown("###")
    bar_chart = df_DISTRITO.TIPO_GESTION.value_counts()
    bar_chart = pd.DataFrame(bar_chart)
    bar_chart.columns = ['Tipo de gestión']
    st.write('**Gráfico 3. Tipo de gestión de las universidades según zona geográfica seleccionada.**')
    st.markdown("###")
    st.bar_chart(bar_chart)
    
    st.markdown("---")
    st.header('Un poco de historia:')
    st.write('Hacia 1959, el Perú contaba con 9 universidades, de las cuales una era de gestión privada. En adelante, el número de universidades incrementó con el Decreto Legislativo Nº 882, Ley de Promoción de la Inversión en la Educación, que permitió la creación y el funcionamiento de universidades privadas con o sin fines de lucro, bajo cualquier forma de organización.')
    st.write('Figura 3. La educación superior universitaria en Perú.')
    image = Image.open('Historia.jpeg')
    st.image(image) 
    st.write("**Fuente**: SUNEDU, 2016.")
    st.subheader('A nivel mundial')
    st.write('A nivel internacional, la calidad de las universidades peruanas es percibida como baja. **Solo una universidad peruana figura entre las 500 mejores universidades del mundo en el QS World University Rankings 2015-2016**. ')
    image = Image.open('ranking_1.jpg')
    st.image(image)
    st.caption('En junio del 2019 fueron publicados los resultados del ranking 2020, donde la PUCP figura nuevamente como líder nacional, posicionándose en el puesto 474 y 17 a nivel mundial y latinoamericano respectivamente.')
    st.markdown("###")
    st.subheader('A nivel de América Latina')
    st.write('Según este ranking, solo tres universidades peruanas figuran entre las 100 mejores de América Latina.')
    image = Image.open('ranking_2.jpeg')
    st.image(image)
    image = Image.open('ranking_3.jpeg')
    st.image(image)
    
#-----------------------------------------------------------------------------------------------------
df_otorgada = pd.read_csv('https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciadas.csv')
df_denegada = pd.read_csv('https://raw.githubusercontent.com/ximenarojo/prueba/main/nolicenciadas.csv')
df_io = pd.read_csv('https://raw.githubusercontent.com/ximenarojo/prueba/main/IO.csv')
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
    option = '-'
    if dataset == 'Licencia otorgada':
        option = 'licencia otorgada'
        st.markdown("###")
        st.write('**Gráfico 3. Universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        @st.cache
        def otorgada_data():
            df_otorgada = pd.read_csv('Licenciadas.csv')
            df_otorgada = df_otorgada.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
            return df_otorgada
        data = otorgada_data()
        st.map(data)        
        st.markdown("###")
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_otorgada)
        n = len(df_otorgada.axes[0]) 
        
    elif dataset == 'Licencia denegada':
        option = 'licencia denegada'
        st.markdown("###")
        st.write('**Gráfico 3. Universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        @st.cache
        def denegada_data():
            df_denegada = pd.read_csv('nolicenciadas.csv')
            df_denegada = df_denegada.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
            return df_denegada
        data = denegada_data()
        st.map(data)
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_denegada)
        n = len(df_denegada.axes[0])
    
    elif dataset == 'Con informe de observaciones (IO) notificado':
        option = 'informe de observaciones (IO) notificado'
        st.markdown("###")
        st.write('**Gráfico 3. Universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        @st.cache
        def io_data():
            df_io = pd.read_csv('IO.csv')
            df_io = df_io.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
            return df_io
        data = io_data()
        st.map(data)
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_io)
        n = len(df_io.axes[0])
        
    elif dataset == 'Ninguno':
        option = 'ningún estado de licenciamiento'
        st.markdown("###")
        st.write('**Gráfico 3. Universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        @st.cache
        def ninguno_data():
            df_ninguno = pd.read_csv('Ninguno.csv')
            df_ninguno = df_ninguno.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
            return df_ninguno
        data = ninguno_data()
        st.map(data)
        
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_ninguno)
        n = len(df_ninguno.axes[0])
     
    st.write('Se encontraron', n,'registros de universidades para su búsqueda.')    
    
#--------------------------------------------------------------------------------------------
if selected == 'Funcionamiento':
    st.markdown("<h1 style ='text-align: center'>Licencia de Funcionamiento Institucional</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write('La Licencia de Funcionamiento Institucional es de carácter temporal y renovable, con una vigencia mínima de seis (6) años, y es otorgada o denegada por el Consejo Directivo de la SUNEDU. Esta se determina en base a una serie de factores, entre los que destaca la promoción de la investigación y los hallazgos que dicha universidad pueda exponer ante la comunidad internacional.')
    st.write('- La Ley Universitaria estableció un periodo mínimo de vigencia de 6 años, al que se suma otro de 8 años y de 10 años.')
    st.markdown("###")
    df = pd.read_csv('Licenciadas.csv')
    col1, col2 = st.columns(2)
    with col1:
        pie_chart = df.PERIODO_LICENCIAMIENTO.value_counts()
        pie_chart = pd.DataFrame(pie_chart)
        pie_chart = pie_chart.reset_index()
        pie_chart.columns = ['PERIODO_LICENCIAMIENTO','TOTAL']
        fig1, ax1 = plt.subplots()
        ax1.pie(pie_chart['TOTAL'], labels = pie_chart['PERIODO_LICENCIAMIENTO'], autopct='%1.1f%%')
        ax1.axis('equal')
        st.write('**Gráfico 4. Período de licenciamiento en años.**')
        st.markdown("###")
        st.pyplot(fig1)
    with col2:
        st.write('Hasta la fecha (31/08/2022), **de las 93** universidades licenciadas, **solo 5** han sido beneficiadas con el tiempo máximo de licenciamiento.')
        image = Image.open('Vigencia.png')
        st.image(image) 
        st.write("**Fuente**: Elaboración propia.")
        
    st.markdown("###")
    st.write('**A continuación, seleccione una opción para visualizar la información.**')
    df = pd.read_csv('Licenciadas.csv')
    periodo = df['PERIODO_LICENCIAMIENTO'].unique().tolist()
    periodo_selec = st.multiselect('A continuación, seleccione solamente un período de licenciamiento:', 
                                   periodo,
                                   default = periodo)
    mask = (df['PERIODO_LICENCIAMIENTO'].isin(periodo_selec))
    n = df[mask].shape[0]
    st.write(f'Se encontraron {n} resultados para su búsqueda.')
    st.markdown("###")

    url = 'https://raw.githubusercontent.com/ximenarojo/prueba/main/Licenciadas.csv'
    datos = pd.read_csv(url, sep=',')
    
     
    #st.line_chart(data=datos, x='NOMBRE', y='PERIODO_LICENCIAMIENTO')
    
    
#--------------------------------------------------------------------------------------------
if selected == 'Equipo':
    st.markdown("<h1 style='text-align: center'>¿Quiénes somos?</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write('Somos estudiantes de 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia, que motivados por los conocimientos adquiridos por el curso de Programación Avanzada y junto a la asesoría de los profesores, hemos desarrollado una app interactiva para la visualización y exploración práctica de los datos recopilados sobre el avance y estatus actual del Licenciamiento Institucional de las Universidades tanto públicas como privadas del Perú.')
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
    with open('message.css') as f:
        st.markdown(f'<style>{f.read()}</message>', unsafe_allow_html=True)
