import pandas as pd
import os
from database import get_connection

def load_posts():
    print("🔥 load_posts() called")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "posts.csv")

    print("CSV PATH:", csv_path)

    df = pd.read_csv(csv_path)
    print("Rows loaded:", len(df))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            userId INTEGER,
            id INTEGER PRIMARY KEY,
            title TEXT,
            body TEXT
        )
    """)

    df.to_sql("posts", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print("✅ posts table created successfully")

if __name__ == "__main__":
    load_posts()
