import unittest
import pandas as pd
import os
import sys

# Add the parent directory to sys.path to import setup_data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setup_data import generate_data

class TestDataLogic(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.csv_path = os.path.join(self.test_dir, "test_sales_data.csv")
        self.db_path = os.path.join(self.test_dir, "test_sales_database.db")

    def tearDown(self):
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_generate_data_columns(self):
        """Test if the generated data has all required columns."""
        n_rows = 10
        generate_data(n_rows=n_rows, base_dir=self.test_dir)
        
        df = pd.read_csv(self.csv_path)
        expected_columns = ['Transaction_ID', 'Customer_Name', 'DOB', 'Purchase_Date', 'Amount', 'Category', 'Age']
        for col in expected_columns:
            self.assertIn(col, df.columns)
        self.assertEqual(len(df), n_rows)

    def test_category_consistency(self):
        """Test if categories are within the expected set."""
        generate_data(n_rows=50, base_dir=self.test_dir)
        df = pd.read_csv(self.csv_path)
        valid_categories = {'Electronics', 'Clothing', 'Home', 'Groceries', 'Beauty'}
        categories_in_data = set(df['Category'].unique())
        self.assertTrue(categories_in_data.issubset(valid_categories))

if __name__ == '__main__':
    unittest.main()
