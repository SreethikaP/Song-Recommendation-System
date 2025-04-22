# src/components/recommendation.py

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from src.logger import logger
from src.exception import CustomException
import sys

class SongRecommender:
    def __init__(self, model_path, data_path, selected_features):
        self.model_path = model_path
        self.data_path = data_path
        self.selected_features = selected_features

        try:
            self.model = joblib.load(self.model_path)
            logger.info(f"Loaded trained model from {self.model_path}")
            
            self.df = pd.read_csv(self.data_path)
            logger.info(f"Loaded dataset from {self.data_path}")
        except Exception as e:
            raise CustomException(e, sys)

    def recommend(self, song_name, top_n=5):
        try:
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(self.df[self.selected_features].dropna())

            cluster_labels = self.model.predict(X_scaled)
            self.df['cluster'] = cluster_labels

            selected_song = self.df[self.df['track_name'].str.lower() == song_name.lower()]
            if selected_song.empty:
                return []

            selected_cluster = selected_song['cluster'].values[0]

            recommended_songs = self.df[self.df['cluster'] == selected_cluster]
            recommended_songs = recommended_songs.sample(n=min(top_n, len(recommended_songs)))

            return recommended_songs[['track_name', 'artist_name']]
        except Exception as e:
            raise CustomException(e, sys)
