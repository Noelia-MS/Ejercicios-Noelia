import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='EDAs', page_icon=':bar_chart:')


st.title('Página EDAs')

if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')

st.header('1. Carga de datos')

st.header('2. Gráficos univariantes')

st.header('3. Gráficos bivariantes')

st.header('4. Gráficos multivariantes')
# sns.lmplot(y="carat", x="price", hue="clarity", data= df, fit_reg= False)


# Cargar el dataframe de diamantes
# Suponiendo que tienes un archivo CSV llamado "diamonds.csv"
df = sns.load_dataset('diamonds')

st.title("Exploración de Datos de Diamantes")

# Mostrar el dataframe
st.subheader("Dataframe de Diamantes")
st.write(df)

# Seleccionar una característica para visualizar
feature = st.selectbox("Selecciona una característica para visualizar", ['carat', 'price', 'depth', 'table', 'x', 'y', 'z'])

# Crear un histograma de la característica seleccionada
st.subheader(f"Histograma de {feature}")
fig, ax = plt.subplots()
sns.histplot(df[feature], kde=True, ax=ax)
st.pyplot(fig)

# Estadísticas descriptivas
st.subheader("Estadísticas Descriptivas")
st.write(df.describe())

# Filtros interactivos
st.subheader("Filtros Interactivos")
cut_filter = st.selectbox("Selecciona el tipo de corte", df['cut'].unique())
color_filter = st.selectbox("Selecciona el color", df['color'].unique())
filtered_df = df[(df['cut'] == cut_filter) & (df['color'] == color_filter)]
st.write(filtered_df)

# Gráfico de dispersión interactivo
st.subheader("Gráfico de Dispersión")
x_axis = st.selectbox("Selecciona el eje X", ['carat', 'depth', 'table', 'price', 'x', 'y', 'z'])
y_axis = st.selectbox("Selecciona el eje Y", ['carat', 'depth', 'table', 'price', 'x', 'y', 'z'])
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x=x_axis, y=y_axis, hue='cut', ax=ax)
st.pyplot(fig)
