import sqlite3

connect = sqlite3.connect('data.db')
connect.row_factory = sqlite3.Row

def create_table():
    with connect:
        connect.execute('CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);')

def add_entry(entry_content, entry_date):
    with connect:
        connect.execute("INSERT INTO entries VALUES(?, ?)", (entry_content, entry_date) )

def get_entries():
    cursor = connect.execute("SELECT * FROM entries;")
    return cursor