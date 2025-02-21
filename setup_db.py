import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    customer_name TEXT,
    purchase_date TEXT,
    FOREIGN KEY (product_id) REFERENCES products (id)
)
''')

conn.commit()
conn.close()

print("Database and tables created successfully.")
