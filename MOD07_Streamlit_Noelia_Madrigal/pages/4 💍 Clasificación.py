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

# Formulario 
st.header('Introduce los datos para la predicción')

with st.form('mi_formulario'):
    carat= st.number_input('Peso en quilates (carat)',
                           min_value=0.10, max_value=5.20,
                           value= 1.00,
                           step= 0.01)
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
    price= st.number_input('Precio (price)',
                           min_value=300.00, max_value=20000.00,
                           value= 3000.00,
                           step= 1.00)
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
    st.metric('Corte estimado', value=f'{corte_estimado}')
    
    
    # Guardar en CSV
    # X_new['corte_estimado'] = corte_estimado
    # archivo_csv = 'clasificacion_diamonds.csv'
    # X_new.to_csv(archivo_csv, index=False)
    
    # with open(archivo_csv, 'rb') as file:
    #     btn = st.download_button(
    #         label='Descargar como CSV',
    #         data=file,
    #         file_name=archivo_csv,
    #         mime='text/csv'
    #     )