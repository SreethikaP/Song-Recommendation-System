# src/components/data_ingestion.py

import pandas as pd
from src.logger import logger
from src.exception import CustomException
import sys

class DataIngestion:
    def __init__(self, data_path):
        self.data_path = data_path

    def initiate_data_ingestion(self):
        try:
            logger.info("Starting data ingestion.")
            df = pd.read_csv(self.data_path)
            logger.info(f"Dataset loaded successfully. Shape: {df.shape}")
            return df
        except Exception as e:
            logger.error("Error occurred during data ingestion.")
            raise CustomException(e, sys)
