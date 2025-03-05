import streamlit as st
import pandas as pd
import seaborn as sns
import joblib

st.set_page_config(page_title='Regresión', 
                   page_icon=':moneybag:')


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

# Session_state
if 'df_pred_price' not in st.session_state:
    st.session_state['df_pred_price'] = pd.DataFrame(columns=[
        'carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z', 'precio_estimado'])

# Formulario 
st.header('Introduce los datos para la predicción')

with st.form('mi_formulario'):
    col1, col2, col3 = st.columns(3)
    with col1:
        carat= st.number_input('Carat',
                           min_value=0.10, max_value=5.20,
                           value= 1.00,
                           step= 0.01)
    with col2:
        depth = st.number_input('Depth',
                            min_value=40.00, max_value=80.00,
                            value=60.00,
                            step= 0.10)
    with col3:
        table = st.number_input('Table',
                            min_value=40.00, max_value=100.00,
                            value= 70.00,
                            step=0.10)

    col4, col5, col6 = st.columns(3)           
    with col4:
        cut = st.selectbox('Cut', ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair'])
        
    with col5:       
        color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])

    with col6:
        clarity = st.selectbox('Clarity', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])

    col7, col8, col9 = st.columns(3)
    with col7:
        x= st.number_input('X',
                            min_value=1.00, max_value=20.00,
                            value=5.50,
                            step= 0.01)   
    with col8:               
        y= st.number_input('Y',
                             min_value=1.00, max_value=60.00,
                            value=5.50,
                            step= 0.01)          
    with col9:
        z= st.number_input('Z',
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
    X_new['precio_estimado'] = round(prediccion, 2)
    st.session_state['df_pred_price'] = pd.concat([st.session_state['df_pred_price'], X_new], 
                                                   ignore_index=True)
    st.metric('Precio estimado', value=f'{prediccion:.2f} $')
    
# Df de predicciones
    st.markdown('Dataframe de predicciones realizadas')
    st.dataframe(st.session_state['df_pred_price'])

# Descargar predicciones como CSV
if not st.session_state['df_pred_price'].empty:
    csv = st.session_state['df_pred_price'].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Descargar predicciones como CSV",
        data=csv,
        file_name='predicciones_precio.csv',
        mime='text/csv'
    )

if st.button('Ir a clasificación'):
    st.switch_page('pages/4 💍 Clasificación.py')