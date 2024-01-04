import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment variables
database_url = os.environ.get('DATABASE_URL')

# Configure the database settings
db_settings = dj_database_url.config(default=database_url, conn_max_age=600, ssl_require=True)

# Try to connect to the database
try:
    import psycopg2
    conn = psycopg2.connect(**db_settings)
    print("Database connection established successfully!")
except Exception as e:
    print(f"Error connecting to the database: {e}")
finally:
    # Close the connection if it was established
    if conn:
        conn.close()
