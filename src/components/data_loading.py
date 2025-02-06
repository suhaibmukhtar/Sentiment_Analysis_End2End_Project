#will contain code realted to loading data from the source

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from logger import logging
import os
from exception import CustomException
import sys

logging.info('Data loading started')
DATA_DIR = os.path.join(os.getcwd(),'src','data')
# Load the data
def load_data(DATA_DIR):
    try:
        data_files = os.listdir(DATA_DIR)
        for file in data_files:
            if 'csv' in file:
                data = pd.read_csv(os.path.join(DATA_DIR, file))
                logging.info(f'{file} loaded successfully')

        logging.info("\nData Characteristics")
        logging.info(f"\nData shape: {data.shape}")
        logging.info(f"\nData columns: {data.columns}")
        logging.info(f"\nMissing Records: {data.isnull().sum()}")
        logging.info(f"\nDuplicate Records: {data.duplicated().sum()}")
        logging.info(f"\nData description: {data.describe()}")
        logging.info(f"\nNumerical Columns: {data.select_dtypes(exclude='O').columns}")
        logging.info(f"\nCategorical Columns: {data.select_dtypes(include='O').columns}")
    except Exception as e:
        raise CustomException(e,sys)
    return data


