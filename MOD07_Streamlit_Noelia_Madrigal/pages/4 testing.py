import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import requests

st.set_page_config(
    page_title="Título aplicación Layout",
    page_icon="🧊", # favicon
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# tabs
tab1, tab2, tab3 = st.tabs(['EDA', 'Regresión', 'Clasificación'])

with tab1:
    st.image('https://placehold.co/600x300', caption='Imagen 600x300')
    # si lo ponemos como imagen directa no será responsive a menos que la hagamos en CSS ni tendría border-radius
    # st.html('<img src="https://placehold.co/600x250" style="text-align:center;">')
    # st.write('Contenido de la primera columna')

with tab2:
    # st.write('Contenido de la segunda columna')
    st.image('https://placehold.co/600x300', caption='Imagen 600x300')
    
with tab3:
    # st.write('Contenido de la tercera columna')
    st.image('https://placehold.co/600x300', caption='Imagen 600x300')
# Se puede agregar archivos statics de css externos
# with open('styles.css') as f:
#     st.html(f'<style>{f.read()}</style>')

# st.title('Elementos para layout y estructura')

# st.header('1. Columnas')
# se puede cambiar la alineación del contenido:
# col1, col2, col3 = st.columns(3, vertical_alignment='bottom')
# col1, col2, col3 = st.columns(3, vertical_alignment='top')

# expander
st.header('Preguntas')

with st.expander('¿Cuál es la calidad del corte del diamante?'):
    st.image('https://shorturl.at/XfAsy', caption='Corte de diamantes')
    
with st.expander('¿Qué colores tienen los diamantes'):
    st.write('''Los colores de los diamantes se clasifican utilizando una escala que va desde la letra D (incoloro) hasta la letra Z (amarillo claro).
             Los diamantes con color "D" son totalmene incoloro y, por lo tanto, más valiosos''')
         

    
with st.expander('Claridad del diamante'):
    st.write('Una escala desde FL (sin imperfecciones internas) hasta I (con inclusiones visibles a simple vista)')
    
# container
st.header('4. container')

container1 = st.container(border=True)
container1.write('Esto es un texto')
container1.write('Esto es otro texto')

container2 = st.container(border=True)
container2.write('Esto es un texto')
container2.image('https://placehold.co/300x200', caption='Imagen 300x200')

container2.write('Esto es otro texto')

