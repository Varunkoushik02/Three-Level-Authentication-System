import sqlite3

def init_db():
    conn = sqlite3.connect("auth.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            pattern TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password, email, pattern):
    conn = sqlite3.connect("auth.db")
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO users (username, password, email, pattern) VALUES (?, ?, ?, ?)",
              (username, password, email, pattern))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect("auth.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return user
