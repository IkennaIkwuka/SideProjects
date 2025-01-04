import sqlite3

conn = sqlite3.connect("tasks_database.db")
print("Database connected successfully")

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS Tasks_Lists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Description TEXT not NULL
    )
"""
)
print("Table created successfully!")
conn.commit()
conn.close()
