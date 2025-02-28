import streamlit as st
import pandas as pd
import seaborn as sns
import joblib
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title='Clasificación', page_icon=':diamond_shape_with_a_dot_inside:')


st.title('Clasificación de Corte de Diamantes')

if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')
    
pipeline_clasificacion = joblib.load('./models/pipeline_clasificacion.joblib')

input_data = {
    'carat': st.number_input('Carat'),
    'color': st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J']),
    'clarity': st.selectbox('Clarity', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']),
    'depth': st.number_input('Depth'),
    'table': st.number_input('Table'),
    'price': st.number_input('Price'),
    'x': st.number_input('X'),
    'y': st.number_input('Y'),
    'z': st.number_input('Z')
}    
    
X_new = pd.DataFrame([input_data])
prediction_encoded = pipeline_clasificacion.predict(X_new)
df= sns.load_dataset('diamonds')
label_encoder = LabelEncoder()
label_encoder.fit(df['cut'])
prediction = label_encoder.inverse_transform(prediction_encoded)
st.write(f'El corte estimado del diamante es: {prediction[0]}')   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# st.write('''La escala de color de los diamantes utiliza letras para clasificarlos, 
#          desde la letra D (incoloro) hasta la letra Z (amarillo claro).
         
#          Incoloro (D-F); Casi incoloro (G-J)
#          Los colores de los diamantes se clasifican utilizando una escala que va desde la letra D hasta la Z,
#         según el Instituto Gemológico de América (GIA), donde la letra "D" es totalmene incoloro y, por lo tanto, más valioso,
         
#          ''')

# st.write('''Cortes de diamante de más a menos, según la calidad:

# Ideal
# Premium
# Very Good
# Good
# Fair

# El corte "Ideal" se considera el mejor, ya que maximiza el brillo del diamante. 
# "Premium" también es excelente y tiene un rendimiento de luz muy cercano al "Ideal".
# "Very Good" sigue siendo un corte de alta calidad, 
# "Good" y "Fair" son cortes menos deseables en términos de brillo y proporción.''')