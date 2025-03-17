import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")
df_songs = pd.read_csv("datasets/topsongs.csv")

rpm_min = df_songs["beats.per.minute"].min()
rpm_max = df_songs["beats.per.minute"].max()

rpm_slider = st.sidebar.slider("RPM Range", rpm_min, rpm_max, rpm_max)
rpm_return = df_songs[df_songs["beats.per.minute"] <= rpm_slider]


st.title('"Top 100 Most Streamed Songs on Spotify"')
st.caption("Esta é uma aplicação de conceitos iniciais estudados em Python - por Henrique A. Florentino")
st.feedback("stars")

rpm_return

st.link_button("Acesse a referência para este banco de dados!", 'https://www.kaggle.com/datasets/pavan9065/top-100-most-streamed-songs-on-spotify?resource=download')


st.divider()

st.title("Gráficos")

fig = px.line(rpm_return["beats.per.minute"], title ='Visão geral do RPM')
fig2 = px.histogram(rpm_return["energy"], title ='Visão geral da Energia' )

col1, col2 = st.columns(2);
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

st.divider()

st.title("Estatística")
st.caption("Esta é uma aplicação de conceitos estudados em estatística verificando a Média, Moda e Mediana de alguns dados aqui apresentados")

rpm_mean = df_songs["beats.per.minute"].mean()
valence_mean = df_songs["valance"].mean()
danceability_mean = df_songs["danceability"].mean()

st.title("Média")

mean_col1, mean_col2, mean_col3 = st.columns(3)
mean_col1.metric("RPM", round(rpm_mean))
mean_col2.metric("Valence", f"{valence_mean:.2f}")
mean_col3.metric("Danceability", f"{danceability_mean:.2f}")

st.divider()

rpm_mode = df_songs["beats.per.minute"].mode()[0]
valence_mode = df_songs["valance"].mode()[0]
danceability_mode = df_songs["danceability"].mode()[0]

st.title("Moda")
mode_col1, mode_col2, mode_col3 = st.columns(3)
mode_col1.metric("RPM", rpm_mode)
mode_col2.metric("Valence", valence_mode)
mode_col3.metric("Danceability", danceability_mode)

st.divider()

rpm_median = df_songs["beats.per.minute"].median()
valence_median = df_songs["valance"].median()
danceability_median = df_songs["danceability"].median()

st.title("Mediana")
median_col1, median_col2, median_col3 = st.columns(3)
median_col1.metric("RPM", rpm_median)
median_col2.metric("Valence", valence_median)
median_col3.metric("Danceability", danceability_median)






