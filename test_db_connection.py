import os
import psycopg2

# Use the DATABASE_URL environment variable
db_url = os.environ.get("DATABASE_URL")

try:
    # Attempt to connect to the database
    conn = psycopg2.connect(db_url)
    print("Connected to the database!")
except Exception as e:
    print(f"Error connecting to the database: {e}")
finally:
    # Close the connection if it was established
    if conn:
        conn.close()
