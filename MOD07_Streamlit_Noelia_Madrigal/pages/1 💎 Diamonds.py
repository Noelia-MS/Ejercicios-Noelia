import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.set_page_config(page_title='Diamonds', page_icon=':gem:')

st.title('Diamonds dataset')


if st.button('Volver a inicio'):
   st.switch_page('🏠Inicio.py')

st.header('Características de los diamantes')

st.image('https://damiancolombo.com/backoffice/images/1860-Educaci%C3%B3n%20-%20Diamantes.jpg', width=400)

st.subheader('El dataset se estructura en:')

container= st.container()
with container:
    container.markdown(''' 
            - **Quilates:** Peso del diamante.
            - **Corte:** Calidad del corte (Fair, Good, Very Good, Premium, Ideal).
            - **Color:** Categorizado desde D hasta J.
            - **Claridad:** Pureza, desde IF hasta I1.
            - **Profundidad:** Relación altura/diametro. 
            - **Mesa:** Ancho de la superficie superior.
            - **Precio:** Precio en dólares.
            - **Ancho (x):** Ancho en mm.
            - **Alto (y):** Alto en mm.
            - **Longitud (z):** Largo en mm.        
            ''')

    with st.expander('¿Cuál es la calidad del corte del diamante?'):
        st.write('''El corte Ideal se considera el mejor. Premium también es excelente. Very Good es de alta calidad.
                Good y Fair son cortes menos deseables.''')
        st.image('https://shorturl.at/XfAsy')
        
    with st.expander('¿Qué colores tienen los diamantes?'):
        st.write('''Se clasifican utilizando una escala que va desde la letra D (incoloro) hasta la letra Z (amarillo claro).
                Los diamantes con color "D", que son totalmene incoloros, son los más valiosos''')
        st.image('https://damiancolombo.com/backoffice/images/color-diamante.jpg', caption='Color')
            
    with st.expander('¿Cómo se mide la pureza de los diamantes?'):
        st.write('''Por sus inclusiones, que son los defectos internos que afectan a la claridad.
                Se categorizan desde IF (sin inclusiones) hasta I1 (inclusiones visibles )''')
        st.image('https://www.tallerdejoyeriamalaga.com/wp-content/uploads/2021/08/escalapureza.png.webp', caption='Claridad')

    if st.checkbox('Entendido'):
        st.balloons()

    
if st.button('Ir a EDAs'):
    st.switch_page('pages/2 📊 EDA.py')
