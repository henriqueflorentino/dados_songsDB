import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

df_songs = pd.read_csv("datasets/topsongs.csv")

songs = df_songs["title"].unique()
song = st.sidebar.selectbox("Songs", songs)

df_song = df_songs[df_songs["title"] == song].iloc[0]  

artist = df_song["artist"]
topgenre = df_song["top genre"]
year = df_song["year"]
rpm = df_song["beats.per.minute"]
energy = df_song["energy"]
danceability = df_song["danceability"]
loudnessdb = df_song["loudness.dB"]
liveness = df_song["liveness"]
valence = df_song["valance"]

st.title(song)
st.header(artist)
st.subheader(topgenre)
st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("Year", year)
col2.metric("RPM", rpm)
col3.metric("Energy", energy)

col4, col5, col6 = st.columns(3)
col4.metric("Danceability", danceability)
col5.metric("Loudness (dB)", loudnessdb)
col6.metric("Liveness", liveness)

st.metric("Valence", valence)
