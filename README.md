Data Engineering Project – Posts Analytics Pipeline
🚀 Project Overview

This project is a complete Data Engineering pipeline that loads data from a CSV file, stores it in a SQLite database, and runs analytical SQL queries using Python and Pandas.

It simulates how real data pipelines work in production environments.

                🗂 Project Structure
        data-engineering-project/
        │
        ├── data/
          │   ├── posts.csv
          │   └── posts.db
        │
        ├── scripts/
        │   ├── database.py
        │   ├── load.py
        │   ├── query.py
        │   └── main.py
        │
        ├── venv/
        └── README.md

⚙️ Technologies Used

Python
Pandas
SQLite
SQL

Virtual Environment (venv)

📥 Data Source

The dataset posts.csv contains:

userId

id

title

body

Each row represents a post made by a user.

🔄 How the Pipeline Works
posts.csv
   ↓
load.py  →  SQLite Database
   ↓
query.py → Data Analysis

▶️ How to Run
1. Activate Virtual Environment
venv\Scripts\activate
2. Load Data
python scripts/load.py
3. Run Queries
python scripts/query.py
4. Run Full Pipeline
python scripts/main.py

📊 Example Query
SELECT userId, COUNT(*) AS total_posts
FROM posts
GROUP BY userId
ORDER BY total_posts DESC;

This query shows how many posts each user created.


🎯 What This Project Shows

Data extraction from CSV
Data loading into a database
SQL analytics
Clean project structure
Real Data Engineering workflow

👨‍💻 Author

Meshal Ahmad
