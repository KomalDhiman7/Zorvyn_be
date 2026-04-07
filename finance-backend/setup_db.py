from config import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    role TEXT,
    is_active BOOLEAN
)
""")

# Create records table
cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    type TEXT,
    category TEXT,
    date TEXT,
    notes TEXT,
    user_id INTEGER
)
""")

conn.commit()
conn.close()

print("Tables created successfully")