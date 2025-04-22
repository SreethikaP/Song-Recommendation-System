# src/components/model_trainer.py

import os
import joblib
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from src.logger import logger
from src.exception import CustomException
import sys
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt

class ModelTrainer:
    def __init__(self, model_save_path, selected_features, mlflow_uri):
        self.model_save_path = model_save_path
        self.selected_features = selected_features
        self.mlflow_uri = mlflow_uri

    def train_model(self, df):
        try:
            logger.info("Starting model training pipeline.")
            
            # Selecting Features
            df_selected = df[self.selected_features].dropna()
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(df_selected)

            # Find Best K (Elbow Method)
            inertia = []
            K = range(2, 11)
            for k in K:
                kmeans = KMeans(n_clusters=k, random_state=42)
                kmeans.fit(X_scaled)
                inertia.append(kmeans.inertia_)

            plt.figure(figsize=(8, 4))
            plt.plot(K, inertia, 'bx-')
            plt.xlabel('k')
            plt.ylabel('Inertia')
            plt.title('Elbow Method For Optimal k')
            os.makedirs("artifacts", exist_ok=True)
            elbow_plot_path = os.path.join("artifacts", "elbow_plot.png")
            plt.savefig(elbow_plot_path)
            plt.close()

            optimal_k = 5  # Later manually adjust by seeing elbow_plot

            logger.info(f"Optimal number of clusters selected: {optimal_k}")

            # Train final model
            final_model = KMeans(n_clusters=optimal_k, random_state=42)
            final_model.fit(X_scaled)

            os.makedirs(os.path.dirname(self.model_save_path), exist_ok=True)
            joblib.dump(final_model, self.model_save_path)

            logger.info(f"Model saved successfully at {self.model_save_path}.")

            # MLflow logging
            mlflow.set_tracking_uri(self.mlflow_uri)
            mlflow.set_experiment("Song Recommendation System")

            with mlflow.start_run():
                mlflow.log_param("optimal_k", optimal_k)
                mlflow.sklearn.log_model(final_model, "kmeans_model")
                mlflow.log_artifact(elbow_plot_path)

            logger.info("Model logged successfully to MLflow.")

        except Exception as e:
            logger.error("Error occurred during model training.")
            raise CustomException(e, sys)
