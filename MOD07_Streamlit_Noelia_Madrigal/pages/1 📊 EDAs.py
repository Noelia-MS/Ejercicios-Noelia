import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(page_title='EDAs', page_icon=':bar_chart:')


st.title('Página EDAs')

if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')

st.header('1. Carga de datos')

st.header('2. Gráficos univariantes')

st.header('3. Gráficos bivariantes')

st.header('4. Gráficos multivariantes')

st.markdown('''Los colores de los diamantes se clasifican utilizando una escala que va desde la letra D hasta la Z,
        según el Instituto Gemológico de América (GIA), donde la letra "D" es totalmene incoloro y, por lo tanto, más valioso,''')