import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(page_title='Inicio', page_icon=':house:')
st.title('Proyecto de análisis de datos y Machine Learning en Streamlit')

st.write("\n")
st.write("\n")

st.subheader('Aplicación de Machine Learning en Streamlit para EDA, regresión y clasificación')

st.write("\n")


st.markdown('''
Este proyecto desarrolla dos modelos de aprendizaje automático para predecir el precio y corte de los diamantes.
El usuario puede ingresar los datos específicos para obtener el precio o una clasificación del diamante.

Herramienta interactiva para realizar un Análisis Exploratorio de Datos (EDA), regresión y clasificación utilizando el conjunto de datos de diamantes. 

Se divide en cuatro secciones:
''')

tab1, tab2, tab3, tab4 = st.tabs(['  **Dataset**  ','  **EDA**  ', '  **Regresión**  ', '  **Clasificación**  '])
with tab1:
    st.write('''Breve descripción de las características principales de los diamantes para conocer mejor el dataset utilizado en el proyecto.''')
    if st.button('Ir a Diamonds'):
        st.switch_page('pages/1 💎 Diamonds.py')
with tab2:
    st.write('''El análisis exploratorio de datos consiste en la visualización de las características de los diamantes
             para entender las relaciones entre las variables y como influyen entre sí.''')
    if st.button('Ir a EDAs'):
        st.switch_page('pages/2 📊 EDAs.py')
with tab3:
    st.write('''Modelo de regresión para predecir el precio de los diamantes.             
    El modelo ya está preparado para indicar el precio del diamante al usuario,
    con los datos que facilite en el formulario. ''')
    if st.button('Ir a Regresión'):
        st.switch_page('pages/3 💰 Regresión.py')
with tab4:
    st.write('Modelo de clasificación para predecir el tipo de corte del diamante.')
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/4 💍 Clasificación.py')
        
        
for _ in range(10):
    st.write('\n')


       
st.caption('https://github.com/Noelia-MS')