#will be responsible for transforming the data into a format that can be used by the model
from logger import logging
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from data_loading import load_data
from sklearn.compose import ColumnTransformer

Data_DIR = os.path.join(os.getcwd(),'src','data')
logging.info('Data transformation started')
data = load_data(Data_DIR)



numerical_pipeline = ColumnTransformer()
#using pipeline to transform the data