# src/pipeline/training_pipeline.py

from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTrainer
from src.utils.common import read_yaml
import os

if __name__ == "__main__":
    config = read_yaml("config/config.yaml")

    # Data Ingestion
    data_ingestion = DataIngestion(data_path=config['data_path'])
    df = data_ingestion.initiate_data_ingestion()

    # Model Training
    model_trainer = ModelTrainer(
        model_save_path=config['model_path'],
        selected_features=config['selected_features'],
        mlflow_uri=config['mlflow_uri']
    )
    model_trainer.train_model(df)
