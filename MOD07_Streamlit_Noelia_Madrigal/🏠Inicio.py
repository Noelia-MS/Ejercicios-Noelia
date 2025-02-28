import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(page_title='Inicio', page_icon=':house:')
st.title('Proyecto de análisis de datos y Machine Learning en Streamlit')

st.header('Página home')
st.subheader('Esto es un sub-encabezado')
st.write('Aplicación de Streamlit para EDA, regresión y clasificación')

st.header('2. tabs')
tab1, tab2, tab3 = st.tabs(['EDA', 'Regresión', 'Clasificación'])
with tab1:
    # si lo ponemos como imagen directa no será responsive a menos que la hagamos en CSS ni tendría border-radius
    # st.html('<img src="https://placehold.co/600x250" style="text-align:center;">')
    # st.write('Contenido de la primera columna')
    st.image('https://placehold.co/600x250', caption='Imagen 600x250')

with tab2:
    # st.write('Contenido de la segunda columna')
    st.image('https://placehold.co/600x300', caption='Imagen 600x300')
    
with tab3:
    # st.write('Contenido de la tercera columna')
    st.image('https://placehold.co/600x200', caption='Imagen 600x200')
    
# Descripción del proyecto
st.markdown('''
Este proyecto presenta una herramienta interactiva para realizar un Análisis Exploratorio de Datos (EDA), regresión y clasificación utilizando el conjunto de datos de diamantes. La herramienta ha sido desarrollada con la biblioteca de Streamlit y se divide en tres secciones principales:

1. **Análisis Exploratorio de Datos (EDA):** En esta sección, exploramos visual y estadísticamente las características de los diamantes. Podrás visualizar distribuciones, correlaciones y otras métricas clave.
2. **Regresión:** Aquí, aplicamos modelos de regresión para predecir el precio de los diamantes basándonos en sus características. Puedes ajustar parámetros y ver el rendimiento del modelo en tiempo real.
3. **Clasificación:** En esta sección, clasificamos los diamantes según diferentes categorías. Podrás evaluar la precisión del modelo y ajustar las variables para mejorar el rendimiento.
''')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("EDA")
    st.write("Análisis exploratorio de datos.")
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1 📊 EDAs.py')

with col2:
    st.subheader("Regresión")
    st.write("Modelo de regresión para predecir el precio.")
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2 🔶 Regresión.py')

with col3:
    st.subheader("Clasificación")
    st.write("Modelo de clasificación para predecir el tipo de corte.")
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3 💠 Clasificación.py')