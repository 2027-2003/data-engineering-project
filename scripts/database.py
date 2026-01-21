import sqlite3

def get_connection(db_path="data/posts.db"):
    return sqlite3.connect(db_path)