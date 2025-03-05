import streamlit as st
import pandas as pd
import seaborn as sns
import joblib
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title='Clasificación', page_icon=':ring:')

st.title('Clasificación')
if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')

st.header('Predicción del corte del diamante')

# Cargo el modelo entrenado
@st.cache_resource
def load_scikit_model():
    return joblib.load('./models/pipeline_clasificacion.joblib')

model = load_scikit_model() 

# Aplico el mismo orden del LabelEncoder original
label_encoder =LabelEncoder()
label_encoder.fit(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])


# Tabla con 5 filas de ejemplo
st.write('Ejemplo de los datos')
diamonds= sns.load_dataset('diamonds')
st.table(diamonds.head())

# Session_state
if 'df_pred_cut' not in st.session_state:
    st.session_state['df_pred_cut'] = pd.DataFrame(columns=[
        'carat', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z', 'corte_estimado'])


# Formulario 
st.header('Introduce los datos para la predicción')

with st.form('mi_formulario'):
    col1, col2, col3= st.columns(3)
    with col1:
        carat= st.number_input('Carat',
                            min_value=0.10, max_value=5.20,
                            value= 1.00,
                            step= 0.01)
    with col2:
        color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    with col3:
        clarity = st.selectbox('Clarity', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])

    col4, col5, col6= st.columns(3)
    with col4:
        depth = st.number_input('Depth',
                            min_value=40.00, max_value=80.00,
                            value=60.00,
                            step= 0.10)
    with col5:
        table = st.number_input('Table',
                                min_value=40.00, max_value=100.00,
                                value= 70.00,
                                step=0.10)
    with col6:
        price= st.number_input('Price',
                            min_value=300.00, max_value=20000.00,
                            value= 3000.00,
                            step= 1.00)

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
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'price': [price],
        'x': [x],
        'y': [y],
        'z': [z]
    })

    prediccion = model.predict(X_new)[0]
    corte_estimado = label_encoder.inverse_transform([prediccion])[0]
    X_new['corte_estimado'] = corte_estimado
    st.session_state['df_pred_cut'] = pd.concat([st.session_state['df_pred_cut'], X_new], 
                                                   ignore_index=True)
    st.metric('Corte estimado', value=f'{corte_estimado}')
   
# Df de predicciones
    st.markdown('Dataframe de predicciones realizadas')
    st.dataframe(st.session_state['df_pred_cut'])
    
# Descargar predicciones como CSV
if not st.session_state['df_pred_cut'].empty:
    csv = st.session_state['df_pred_cut'].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Descargar predicciones como CSV",
        data=csv,
        file_name='predicciones_corte.csv',
        mime='text/csv'
    )