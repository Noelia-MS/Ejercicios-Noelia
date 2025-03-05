import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title='EDA', page_icon=':bar_chart:')


st.title('Análisis Exploratorio de Datos')
if st.button('Volver a inicio'):
    st.switch_page('🏠Inicio.py')


# Carga de datos y mostrar df
st.subheader('Visualización del dataset')
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
mostrar_estadisticas = st.checkbox('Mostrar u ocultar estadísticas')
if mostrar_estadisticas:
    st.write(df.describe().round(2))

# Filtros en sidebar
st.sidebar.header('Filtros')
cortes = df['corte'].unique().tolist()
selected_cortes = st.sidebar.multiselect('Selecciona uno o varios cortes:', options=cortes, default=cortes)

colores = df['color'].unique().tolist()
selected_colores = st.sidebar.multiselect('Selecciona uno o varios colores:', options=colores, default=colores)

claridad = df['claridad'].unique().tolist()
selected_claridad = st.sidebar.multiselect('Selecciona uno o varios tipos de claridad:',
                                   options=claridad, default=claridad)

df_filtered = df[
    (df['corte'].isin(selected_cortes)) & 
    (df['color'].isin(selected_colores)) &
    (df['claridad'].isin(selected_claridad))
]

num_feature = st.sidebar.selectbox('🔢 Selecciona la característica numérica:', 
                           ['precio', 'quilate', 'profundidad', 'mesa', 'x', 'y', 'z'])

min_value, max_value = st.sidebar.slider(f'🧮 Selecciona el intervalo para filtrar por {num_feature}:',
                                 df[num_feature].min(), df[num_feature].max(), 
                                 (df[num_feature].min(), df[num_feature].max()))

cat_feature = st.sidebar.radio('🅰️ Selecciona la característica categórica:', 
                       ['corte', 'color', 'claridad'])

df_final = df_filtered[(df_filtered[num_feature] >= min_value) &
                          (df_filtered[num_feature] <= max_value)]

st.subheader('Análisis gráfico')
st.markdown(''' Los gráficos son dinámicos y se actualizarán según la variable que se seleccione
            en el panel lateral.''')

# Gráficos univariantes
with st.expander('Univariante'):
    tab1, tab2, tab3, tab4 = st.tabs(["Histograma", "Curva de Densidad", "Boxplot", "Pie"])

    with tab1:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df_final[num_feature], ax=ax, bins=30, edgecolor='black')
        ax.set_title(f'Histograma de {num_feature}')
        st.pyplot(fig)

    with tab2:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.kdeplot(df_final[num_feature], ax=ax, shade=True)
        ax.set_title(f'Curva de densidad de {num_feature}')
        st.pyplot(fig)

    with tab3:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(df_final[num_feature], ax=ax, showmeans=True)
        ax.set_title(f'Boxplot de {num_feature}')
        st.pyplot(fig)

    with tab4:
        fig = px.pie(df_final, names=cat_feature, title=f'Distribución de {cat_feature}')
        st.plotly_chart(fig)


# Gráficos bivariantes
with st.expander('Bivariante'):
    df_biv_mean = df_final.groupby(cat_feature).agg(mean_value=(num_feature, 'mean')).reset_index()
    fig = px.bar(df_biv_mean, x=cat_feature, y='mean_value',
                title=f'{num_feature.capitalize()} por {cat_feature}', 
                labels={'mean_value': f'{num_feature} promedio'})
    st.plotly_chart(fig)


# Gráficos multivariantes
with st.expander('Multivariante'):
    tab1, tab2, tab3 = st.tabs(['Scatter', 'Heatmap', 'Pairplot'])
    with tab1:
        selected_features = st.multiselect('Selecciona dos características numéricas para el gráfico de dispersión:', 
                                        ['precio', 'quilate', 'profundidad', 'mesa', 'x', 'y', 'z'], 
                                        default=['precio', 'quilate'])

        if len(selected_features) == 2:
            x_feature = selected_features[0]
            y_feature = selected_features[1]

            fig = px.scatter(df_final, x=x_feature, y=y_feature, color=cat_feature,
                            title=f'Gráfico de dispersión de {x_feature.capitalize()} vs {y_feature.capitalize()} por {cat_feature}',
                            labels={x_feature: x_feature.capitalize(), y_feature: y_feature.capitalize()})
            st.plotly_chart(fig)
        else:
            st.write('Por favor, selecciona dos características.')

    with tab2:
        fig, ax = plt.subplots()
        sns.heatmap(df_final.corr(numeric_only=True).round(2), annot=True, cmap='rainbow', ax=ax)
        ax.set_title('Mapa de la relación entre las variables')
        st.pyplot(fig)


    with tab3:      
        fig = px.scatter_matrix(df_final.sample(500).assign(xyz=lambda df: df['x'] * df['y'] * df['z']), 
                                dimensions=['quilate', 'precio', 'profundidad', 'mesa', 'xyz'],
                                color=cat_feature,
                                title=f'Matriz de dispersión de las variables numéricas agrupadas por {cat_feature}')
        fig.update_layout(width=600, height=600)
        st.plotly_chart(fig)



st.write(f'Datos eliminados con los filtros aplicados: **{df.shape[0] - df_final.shape[0]}**')


st.subheader('Descarga el dataset original o con los filtros actuales')

col1, col2, col3 = st.columns(3, vertical_alignment='center')

with col1:
    st.download_button(
        '💾Descargar datos originales',
        data=df.to_csv(index=False),
        file_name='diamonds.csv',
        mime='text/csv'
    ) 
    
with col3:    
    st.download_button(
        '💾Descargar datos filtrados',
        data=df_final.to_csv(index=False), 
        file_name='diamonds_filtered.csv',
        mime='text/csv'
    )

for _ in range(4):
    st.write('\n')

if st.button('Ir a regresión'):
    st.switch_page('pages/3 💰 Regresión.py')