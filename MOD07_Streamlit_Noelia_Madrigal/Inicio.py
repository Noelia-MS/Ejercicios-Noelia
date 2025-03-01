import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(page_title='Inicio', page_icon=':house:')
st.title('Proyecto de análisis de datos y Machine Learning en Streamlit')

st.write("\n")
st.write("\n")

st.subheader('Aplicación de Machine Learning: Streamlit para EDA, regresión y clasificación')

st.write("\n")


st.markdown('''
Este proyecto presenta una herramienta interactiva para realizar un Análisis Exploratorio de Datos (EDA), regresión y clasificación utilizando el conjunto de datos de diamantes. 
La herramienta ha sido desarrollada con la biblioteca de Streamlit y se divide en tres secciones principales:
''')

tab1, tab2, tab3 = st.tabs(['  **EDA**  ', '  **Regresión**  ', '  **Clasificación**  '])
with tab1:
    st.write('El análisis exploratorio de datos consiste en la visualización de las características de los diamantes.')
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1 📊 EDAs.py')
with tab2:
    st.write('Modelo de regresión para predecir el precio de los diamantes. ')
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2 🔶 Regresión.py')
with tab3:
    st.write('Modelo de clasificación para predecir el tipo de corte del diamante.')
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3 💠 Clasificación.py')
        
        
for _ in range(10):
    st.write('\n')



       
st.caption('https://github.com/Noelia-MS')