import streamlit as st
import pandas as pd
import seaborn as sns
import joblib



@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline_regresion.joblib')
 
st.set_page_config(page_title='Regresión', 
                   page_icon=':large_orange_diamond:')


st.title('Regresión')

if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')

# 1. Mostrar datos (opcional)
st.write('Ejemplo de los datos')
df= sns.load_dataset('diamonds')
price_mean= df['price'].mean()
st.table(df.head())


# # 2. Formulario para predicción
# st.header('Introduce datos para la predicción')

# with st.form('mi_formulario'):
#     total_bill = st.number_input('Introduce total cuenta (total_bill)',
#                 min_value=0.0, max_value=100.00,
#                 value=df['total_bill'].mean(),
#                 step=1.0
#                 )
#     size = st.number_input(
#     'Introduce número comensales (size)',
#     min_value=1,
#     value=df['size'].mode()[0],
#     max_value=10,
#     step=1
#     )
#     sex= st.radio('Introduce género (sex)', ['Male', 'Female'])
#     smoker= st.radio('Introduce si es fumador (smoker)', ['Yes', 'No'])
#     day= st.selectbox('Introduce día semana (day)', ['Thur', 'Fri', 'Sat', 'Sun'])
#     time= st.radio('Introduce horario (time)', ['Lunch', 'Dinner'])
    
#     boton_enviar= st.form_submit_button('Enviar')
    
#     if boton_enviar:
#         X_new= pd.DataFrame({
#             'total_bill': [total_bill],
#             'sex': [sex],
#             'smoker': [smoker],
#             'day': [day],
#             'time': [time],
#             'size': [size]
#         })
#         prediccion = model.predict(X_new)[0]
#         delta_value = prediccion - tip_mean
#         col1, col2 = st.columns(2)
#         col1.metric('Propina estimada (predicción)', value=f'{prediccion:.2f} $', delta=f'{delta_value:.2f} $')
#         col2.metric('Propina media', value=f'{tip_mean:.2f} $')
        