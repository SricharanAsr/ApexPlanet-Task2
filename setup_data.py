import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sqlite3
import os
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Set seed for reproducibility
np.random.seed(42)

def generate_data(n_rows=500, base_dir=None):
    """
    Generates synthetic sales data and saves it to a CSV file and a SQLite database.
    
    Args:
        n_rows (int): The number of rows of data to generate. Defaults to 500.
        base_dir (str): The directory to save files in. Defaults to current directory.
    """
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(base_dir):
        try:
            os.makedirs(base_dir)
            logger.info(f"Created directory: {base_dir}")
        except Exception as e:
            logger.error(f"Failed to create directory {base_dir}: {e}")
            sys.exit(1)

    if not os.access(base_dir, os.W_OK):
        logger.error(f"Directory {base_dir} is not writable.")
        sys.exit(1)

    categories = ['Electronics', 'Clothing', 'Home', 'Groceries', 'Beauty']
    names = ['John Doe', 'Jane Smith', 'Bob Brown', 'Alice White', 'Charlie Black', 
             'Elena Gilbert', 'Damon Salvatore', 'Stefan Salvatore', 'Bonnie Bennett', 
             'Caroline Forbes', 'Matt Donovan', 'Tyler Lockwood', 'Alaric Saltzman']
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    logger.info(f"Generating {n_rows} rows of synthetic sales data...")
    
    for i in range(1, n_rows + 1):
        transaction_id = 1000 + i
        customer_name = np.random.choice(names)
        
        # Random DOB between 18 and 64 years ago
        years_ago = np.random.randint(18, 64)
        dob = datetime.now() - timedelta(days=years_ago*365 + np.random.randint(0, 365))
        
        # Purchase date in 2023-2024
        purchase_date = start_date + timedelta(days=np.random.randint(0, 450))
        
        # Amount based on category
        cat = np.random.choice(categories)
        if cat == 'Electronics':
            amount = np.random.uniform(100, 2000)
        elif cat == 'Clothing':
            amount = np.random.uniform(20, 300)
        elif cat == 'Home':
            amount = np.random.uniform(50, 1000)
        else:
            amount = np.random.uniform(5, 150)
            
        data.append({
            'Transaction_ID': transaction_id,
            'Customer_Name': customer_name,
            'DOB': dob.strftime('%Y-%m-%d'),
            'Purchase_Date': purchase_date.strftime('%Y-%m-%d'),
            'Amount': round(amount, 2),
            'Category': cat
        })
        
    df = pd.DataFrame(data)
    
    # Calculate Age
    current_year = datetime.now().year
    df['Age'] = df['DOB'].apply(lambda d: current_year - datetime.strptime(d, '%Y-%m-%d').year)
    
    # Save to CSV
    csv_path = os.path.join(base_dir, "sales_data.csv")
    try:
        df.to_csv(csv_path, index=False)
        logger.info(f"Successfully saved data to CSV: {csv_path}")
    except Exception as e:
        logger.error(f"Failed to save CSV: {e}")
    
    # Create SQLite DB
    db_path = os.path.join(base_dir, "sales_database.db")
    try:
        with sqlite3.connect(db_path) as conn:
            df.to_sql('sales', conn, if_exists='replace', index=False)
        logger.info(f"Successfully created SQLite database: {db_path}")
    except Exception as e:
        logger.error(f"Failed to create SQLite database: {e}")

if __name__ == "__main__":
    # Use environment variable or default to project root
    target_dir = os.getenv("DATA_DIR", r"d:\sricharan-A\documents\Apex_Software_solutions\T2")
    generate_data(1000, base_dir=target_dir)

