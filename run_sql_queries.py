import sqlite3
import pandas as pd
import os
import logging
import argparse
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_queries(db_path, sql_path, output_path):
    """
    Executes SQL queries from a file against a SQLite database and saves results.

    Args:
        db_path (str): Path to the SQLite database file.
        sql_path (str): Path to the SQL file containing queries.
        output_path (str): Path to the text file where results will be saved.
    """
    if not os.path.exists(db_path):
        logger.error(f"Database not found at {db_path}")
        return

    if not os.path.exists(sql_path):
        logger.error(f"SQL file not found at {sql_path}")
        return

    logger.info(f"Starting SQL query execution using {db_path}...")
    
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_path, 'r') as f:
                sql_content = f.read()
            
            # Split queries by semicolon and remove empty ones
            queries = [q.strip() for q in sql_content.split(';') if q.strip()]
            
            with open(output_path, 'w') as out:
                out.write(f"SQL QUERY EXECUTION REPORT - {datetime.now()}\n")
                out.write("="*50 + "\n\n")
                
                for i, query in enumerate(queries, 1):
                    logger.info(f"Executing Query {i}...")
                    out.write(f"--- Query {i} ---\n")
                    
                    # Extract comments for documentation in the output
                    lines = query.split('\n')
                    actual_query = ""
                    for line in lines:
                        if line.strip().startswith('--'):
                            out.write(line + '\n')
                        else:
                            actual_query += line + '\n'
                    
                    out.write("-" * 20 + "\n")
                    
                    try:
                        df = pd.read_sql_query(query, conn)
                        if df.empty:
                            out.write("Result: No rows returned.\n")
                        else:
                            out.write(df.to_string(index=False))
                        out.write("\n\n")
                    except Exception as e:
                        logger.error(f"Error in Query {i}: {e}")
                        out.write(f"ERROR: {e}\n\n")
        
        logger.info(f"SQL execution complete. Results saved to {output_path}")
        
    except Exception as e:
        logger.error(f"General error during query execution: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run SQL queries against a SQLite database.")
    parser.add_argument("--db", default="sales_database.db", help="Path to SQLite database")
    parser.add_argument("--sql", default="business_queries.sql", help="Path to SQL file")
    parser.add_argument("--out", default="sql_results.txt", help="Path to output results file")
    
    args = parser.parse_args()
    
    # Resolve paths relative to the script location if needed
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_p = os.path.join(base_dir, args.db) if not os.path.isabs(args.db) else args.db
    sql_p = os.path.join(base_dir, args.sql) if not os.path.isabs(args.sql) else args.sql
    out_p = os.path.join(base_dir, args.out) if not os.path.isabs(args.out) else args.out
    
    run_queries(db_p, sql_p, out_p)

