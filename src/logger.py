import logging
from datetime import datetime
import os

LOGS_DIR = 'logs'
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
Log_file = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'

Log_file_path = os.path.join(LOGS_DIR, Log_file)

logging.basicConfig(
    filename=Log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(message)s - %(levelname)s - %(lineno)d'
    )

if __name__ == "__main__":
    logging.info("Logger object has been initialized")