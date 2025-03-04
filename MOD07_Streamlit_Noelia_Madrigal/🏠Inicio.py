import streamlit as st

st.set_page_config(page_title='Inicio', page_icon=':house:')
st.title('Proyecto de análisis de datos y Machine Learning en Streamlit')

st.write("\n")
st.write("\n")

st.subheader('Aplicación de EDA, regresión y clasificación')

st.write("\n")


st.markdown('''
Este proyecto ha sido creado para aplicar los conocimientos adquiridos en el Bootcamp de Data Science
de Hack a Boss, integrando los módulos de Python, Machine Learning y Streamlit.

La aplicación web interactiva permite al usuario navegar entre las distintas secciones, 
visualizar un análisis personalizado mediante la aplicación de filtros y obtener predicciones
basadas en modelos de machine learning previamente entrenados.


Se divide en cuatro secciones:
''')

tab1, tab2, tab3, tab4 = st.tabs(['  **Dataset**  ','  **EDA**  ', '  **Regresión**  ', '  **Clasificación**  '])
with tab1:
    st.write('''Breve descripción de las características principales de los diamantes 
             para familiarizarse con el dataset trabajado en el proyecto.''')
    if st.button('Ir a Diamonds'):
        st.switch_page('pages/1 💎 Diamonds.py')
with tab2:
    st.write('''El análisis exploratorio de datos consiste en la visualización de las características
             de los diamantes para entender las relaciones entre las variables y como influyen entre sí.''')
    if st.button('Ir a EDA'):
        st.switch_page('pages/2 📊 EDA.py')
with tab3:
    st.write('''Modelo de regresión entrenado para predecir el precio de los diamantes.
             Con los datos proporcionados por el usuario en el formulario,
             generará una predicción del precio del diamante.''')
    if st.button('Ir a Regresión'):
        st.switch_page('pages/3 💰 Regresión.py')
with tab4:
    st.write('''Modelo de clasificación entrenado para predecir el tipo de corte del diamante.
             Basado en las características ingresadas por el usuario, 
             el modelo determinará la categoría del corte.''')
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/4 💍 Clasificación.py')
        
 
 
        
for _ in range(5):
    st.write('\n')


       
st.caption('https://github.com/Noelia-MS')