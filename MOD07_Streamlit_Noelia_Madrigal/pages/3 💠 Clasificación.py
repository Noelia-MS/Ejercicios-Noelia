import streamlit as st
import pandas as pd
import seaborn as sns
import joblib

st.set_page_config(page_title='Clasificación', page_icon=':diamond_shape_with_a_dot_inside:')


st.title('Clasificación')

if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')