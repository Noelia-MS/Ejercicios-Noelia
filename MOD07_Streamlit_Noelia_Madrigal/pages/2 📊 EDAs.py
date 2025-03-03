import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title='EDAs', page_icon=':bar_chart:')


st.title('Análisis Exploratorio de Datos')
if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')


# Carga de datos y mostrar df
st.header('Visualización del dataset')
df = sns.load_dataset('diamonds')
for col in ['x', 'y', 'z']:
    df[col] = df[col].replace(0, df[col].mean())

df.rename(columns={
    'carat': 'quilate',
    'cut': 'corte',
    'clarity': 'claridad',
    'depth': 'profundidad',
    'table': 'mesa',
    'price': 'precio'}, inplace=True)
    
    
placeholder= st.empty()
placeholder.table(df.head())

col1, col2 = st.columns([1, 1])

with col1:
    clicked = st.button('Mostrar dataframe completo')

if clicked:
    placeholder.dataframe(df, use_container_width=True)
    
    with col2:
        if st.button('Volver a tabla estática'):
            placeholder.table(df.head())

# Describe
st.subheader('Estadísticas de las variables numéricas')
st.write(df.describe().round(2))

# Gráficos univariante
st.header('Análisis univariante')
st.subheader('🔢 Numéricas')
num_feature = st.selectbox('Selecciona la característica numérica a analizar:', 
                           ['precio', 'quilate', 'profundidad', 'mesa', 'x', 'y', 'z'])

st.subheader('🅰️ Categóricas')
cat_feature = st.radio('Selecciona la característica categórica a analizar:', 
                       ['corte', 'color', 'claridad'])

min_value, max_value = st.slider(f'Selecciona el rango para {num_feature}:',
                                 df[num_feature].min(), df[num_feature].max(), 
                                 (df[num_feature].min(), df[num_feature].max()))

df_num_filt = df[(df[num_feature] >= min_value) & (df[num_feature] <= max_value)]
df_filtered= df_num_filt[[num_feature, cat_feature]]

    # Histograma
fig, ax= plt.subplots(figsize=(6,4))
sns.histplot(df_filtered[num_feature], ax=ax, bins=30, edgecolor='black')
ax.set_title(f'Histograma de {num_feature}')
ax.set_xlabel(num_feature)
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

    # KDEplot
fig, ax = plt.subplots(figsize=(6, 4))
sns.kdeplot(df_filtered[num_feature], ax=ax, shade=True)
ax.set_title(f'Curva de densidad de {num_feature}')
ax.set_xlabel(num_feature)
ax.set_ylabel('Densidad')
st.pyplot(fig)

    # Boxplot
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(df_filtered[num_feature], ax=ax, showmeans=True)
ax.set_title(f'Boxplot de {num_feature}')
ax.set_xlabel(num_feature)
ax.set_ylabel('Valor')
st.pyplot(fig)

    # Pie categórico
fig = px.pie(df_filtered, names=cat_feature, title=f'Distribución de {cat_feature}')
st.plotly_chart(fig)

# Gráficos bivariantes
st.header('Análisis bivariante')
    # Gráfico de barras
df_biv_mean = df_filtered.groupby(cat_feature).agg(mean_value=(num_feature, 'mean')).reset_index()
fig = px.bar(df_biv_mean, x=cat_feature, y='mean_value',
             title=f'{num_feature.capitalize()} por {cat_feature}', 
             labels={'mean_value': f'{num_feature} promedio'})
st.plotly_chart(fig)

# Gráficos multivariantes
st.header('Análisis multivariante')

selected_features = st.multiselect('Selecciona dos características numéricas para el gráfico de dispersión:', 
                                   ['precio', 'quilate', 'profundidad', 'mesa', 'x', 'y', 'z'], 
                                   default=['precio', 'quilate'])

if len(selected_features) == 2:
    x_feature = selected_features[0]
    y_feature = selected_features[1]

    fig = px.scatter(df, x=x_feature, y=y_feature, color=cat_feature,
                     title=f'Gráfico de dispersión de {x_feature.capitalize()} vs {y_feature.capitalize()} por {cat_feature}',
                     labels={x_feature: x_feature.capitalize(), y_feature: y_feature.capitalize()})
    st.plotly_chart(fig)
else:
    st.write("Por favor, selecciona al menos dos características para el gráfico de dispersión.")













    # Scatter
# fig, ax= plt.subplots(figsize= (6,4))
# sns.scatterplot(df.sample(2000), x='quilate', y='precio', hue='corte', ax=ax)
# ax.set_title('Relación entre precio y quilates')
# ax.set_xlabel('quilates')
# ax.set_ylabel('precio')
# ax.legend()
# st.pyplot(fig)

    # Heatmap
fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True).round(2), annot=True, cmap='rainbow', ax=ax)
ax.set_title('Mapa de la relación entre las variables')
st.pyplot(fig)

    # Pairplot
fig= sns.pairplot(df.sample(500), hue='corte', palette='viridis')
st.pyplot(fig)




st.subheader('Descarga el dataset original o con los filtros actuales')

col1, col2, col3 = st.columns(3, vertical_alignment='center')

with col1:
    st.download_button(
        'Descargar datos originales',
        data=df.to_csv(index=False),
        file_name='diamonds.csv',
        mime='text/csv'
    ) 
    
with col3:    
    st.download_button(
        'Descargar datos filtrados',
        data=df_filtered.to_csv(index=False), 
        file_name='diamonds_filtered.csv',
        mime='text/csv'
    )

for _ in range(4):
    st.write('\n')

if st.button('Ir a regresión'):
    st.switch_page('pages/3 💰 Regresión.py')
