import sqlite3

DB_NAME = 'calc.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS calc
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        num1 DOUBLE(1, 2) NOT NULL,
        num2 DOUBLE(1, 2) NOT NULL,
        result DOUBLE(1, 2) NOT NULL
    )
''')


conn.commit()

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()