# app.py

import streamlit as st
from src.components.recommendation import SongRecommender
from src.utils.common import read_yaml

# Load Config
config = read_yaml("config/config.yaml")

# Initialize Recommender
recommender = SongRecommender(
    model_path=config['model_path'],
    data_path=config['data_path'],
    selected_features=config['selected_features']
)

# Streamlit Frontend
st.set_page_config(page_title="🎵 Spotify Song Recommendation", layout="wide")

st.title("🎵 Spotify Song Recommendation System")
st.markdown("#### Select a song and get similar song recommendations!")

# Dropdown to select a song
all_songs = recommender.df['track_name'].dropna().unique().tolist()
selected_song = st.selectbox("Choose a Song 🎧", all_songs)

if st.button("Recommend Similar Songs"):
    if selected_song:
        recommendations = recommender.recommend(selected_song, top_n=5)
        
        if len(recommendations) == 0:
            st.warning("❗ Song not found in cluster.")
        else:
            st.success(f"🎶 Songs similar to: **{selected_song}**")
            for idx, row in recommendations.iterrows():
                st.write(f"🎵 {row['track_name']} by {row['artist_name']}")
