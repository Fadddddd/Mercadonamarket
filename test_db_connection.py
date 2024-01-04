import os
import django
from django.db import connections

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectmercadona.settings')
django.setup()

# Test the default database connection
try:
    connection = connections['default']
    connection.connect()
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection error: {e}")
