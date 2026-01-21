from database import get_connection
import pandas as pd

def run_queries():
    conn = get_connection()

    query = """
    SELECT userId, COUNT(*) as total_posts
    FROM posts
    GROUP BY userId
    ORDER BY total_posts DESC
    """

    df = pd.read_sql(query, conn)
    print(df)

    conn.close()


if __name__ == "__main__":
    run_queries()