import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sqlite3
import os

# Set seed for reproducibility
np.random.seed(42)

# Directory for Task 2
base_dir = r"d:\sricharan-A\documents\Apex_Software_solutions\T2"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

def generate_data(n_rows=500):
    categories = ['Electronics', 'Clothing', 'Home', 'Groceries', 'Beauty']
    names = ['John Doe', 'Jane Smith', 'Bob Brown', 'Alice White', 'Charlie Black', 
             'Elena Gilbert', 'Damon Salvatore', 'Stefan Salvatore', 'Bonnie Bennett', 
             'Caroline Forbes', 'Matt Donovan', 'Tyler Lockwood', 'Alaric Saltzman']
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(1, n_rows + 1):
        transaction_id = 1000 + i
        customer_name = np.random.choice(names)
        
        # Random DOB between 1960 and 2005
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
    df.to_csv(csv_path, index=False)
    print(f"Generated {n_rows} rows of data at {csv_path}")
    
    # Create SQLite DB
    db_path = os.path.join(base_dir, "sales_database.db")
    conn = sqlite3.connect(db_path)
    df.to_sql('sales', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Created SQLite database at {db_path}")

if __name__ == "__main__":
    generate_data(1000)
