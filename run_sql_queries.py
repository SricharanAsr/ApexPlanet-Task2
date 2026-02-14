import sqlite3
import pandas as pd
import os

base_dir = r"d:\sricharan-A\documents\Apex_Software_solutions\T2"
db_path = os.path.join(base_dir, "sales_database.db")
sql_path = os.path.join(base_dir, "business_queries.sql")
output_path = os.path.join(base_dir, "sql_results.txt")

def run_queries():
    conn = sqlite3.connect(db_path)
    
    with open(sql_path, 'r') as f:
        sql_content = f.read()
    
    # Split queries by semicolon
    queries = [q.strip() for q in sql_content.split(';') if q.strip()]
    
    with open(output_path, 'w') as out:
        for i, query in enumerate(queries, 1):
            out.write(f"--- Query {i} ---\n")
            # Get the comment block before the query if possible for context
            lines = query.split('\n')
            query_text = ""
            for line in lines:
                if line.startswith('--'):
                    out.write(line + '\n')
                else:
                    query_text += line + '\n'
            
            try:
                df = pd.read_sql_query(query, conn)
                out.write(df.to_string(index=False))
                out.write("\n\n")
            except Exception as e:
                out.write(f"Error executing query: {e}\n\n")
                
    conn.close()
    print(f"SQL results saved to {output_path}")

if __name__ == "__main__":
    run_queries()
