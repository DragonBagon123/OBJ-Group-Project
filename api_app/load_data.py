import sqlite3
import pandas as pd
import os

####Creates database in the same folder as this file (api_app)
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "babynames.db")
conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    sex TEXT,
    count INTEGER,
    year INTEGER
)
""")

# Make sure your SSA files are in a folder named names
for year in range(1880, 2024):
    file = f"yob{year}.txt"
    print(f"Loading year {year}...")  ##Shows progress of database loading
    if os.path.exists(file):
        df = pd.read_csv(file, names=["name", "sex", "count"])

        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO names(name, sex, count, year) VALUES (?, ?, ?, ?)",
                (row["name"], row["sex"], int(row["count"]), year)
            )

conn.commit()
conn.close()

print("Database loaded successfully.")
