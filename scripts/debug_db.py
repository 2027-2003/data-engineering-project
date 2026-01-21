from database import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

conn.close()
