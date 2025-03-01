import streamlit as st
import pandas as pd
import seaborn as sns
import joblib

st.set_page_config(page_title='Regresión', 
                   page_icon=':large_orange_diamond:')


@st.cache_resource
def load_scikit_model():
    return joblib.load('./models/pipeline_regresion.joblib')

model = load_scikit_model() 

st.title('Regresión')
if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')

st.header('Predicción del precio del diamante')


# Mostrar datos
st.write('Ejemplo de los datos')
diamonds= sns.load_dataset('diamonds')
st.table(diamonds.head())


# Formulario 
st.header('Introduce los datos para la predicción')

with st.form('mi_formulario'):
    carat= st.number_input('Peso en quilates (carat)',
                           min_value=0.10, max_value=5.20,
                           value= 1.00,
                           step= 0.01)
    cut = st.selectbox('Calidad del corte (cut)', ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair'])
    color = st.selectbox('Grado de color (color)', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    clarity = st.selectbox('Grado de claridad (clarity)', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])
    depth = st.number_input('Proporción de la profundidad (depth)',
                            min_value=40.00, max_value=80.00,
                            value=60.00,
                            step= 0.10)
    table = st.number_input('Mesa o superficie (table)',
                            min_value=40.00, max_value=100.00,
                            value= 70.00,
                            step=0.10)
    x= st.number_input('Ancho horizontal en mm (eje X)',
                            min_value=1.00, max_value=20.00,
                            value=5.50,
                            step= 0.01)                  
    y= st.number_input('Altura vertical en mm (eje Y)',
                             min_value=1.00, max_value=60.00,
                            value=5.50,
                            step= 0.01)                        
    z= st.number_input('Profundidad en mm (eje Z)',
                            min_value=1.00, max_value=40.00,
                            value=3.50,
                            step= 0.01)                       
          
    boton_enviar= st.form_submit_button('Predecir', type='primary')

if boton_enviar:
    X_new = pd.DataFrame({
        'carat': [carat],
        'cut': [cut],
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z]
    })

    prediccion = model.predict(X_new)[0]
    st.metric('Precio estimado', value=f'{prediccion:.2f} $')
    X_new['precio_estimado'] = round(prediccion,2)