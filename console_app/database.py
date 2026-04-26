import sqlite3
import csv
import os

DB_NAME = "babynames.db"


class BabyNameDatabase:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS babynames (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        sex TEXT NOT NULL,
                        count INTEGER NOT NULL,
                        year INTEGER NOT NULL
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            print("Database error while creating table:", e)

    def load_csv_data(self, file_path):
        if not os.path.exists(file_path):
            print("CSV file was not found.")
            return

        try:
            with self.connect() as conn:
                cursor = conn.cursor()

                with open(file_path, "r", newline="", encoding="utf-8") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        cursor.execute("""
                            INSERT INTO babynames (name, sex, count, year)
                            VALUES (?, ?, ?, ?)
                        """, (
                            row["name"].strip(),
                            row["sex"].strip(),
                            int(row["count"]),
                            int(row["year"])
                        ))

                conn.commit()
                print("CSV data loaded successfully.")

        except sqlite3.Error as e:
            print("Database error while loading CSV:", e)
        except Exception as e:
            print("Error loading CSV:", e)

    def add_name(self, name, sex, count, year):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO babynames (name, sex, count, year)
                    VALUES (?, ?, ?, ?)
                """, (name, sex, count, year))
                conn.commit()
                print("Name record added successfully.")
        except sqlite3.Error as e:
            print("Database error while adding name:", e)

    def search_name(self, name):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, name, sex, count, year
                    FROM babynames
                    WHERE LOWER(name) = LOWER(?)
                    ORDER BY year ASC
                """, (name,))
                results = cursor.fetchall()

                if not results:
                    print("No records found for that name.")
                    return

                print(f"\nRecords for {name}:")
                for row in results:
                    print(f"ID: {row[0]} | Name: {row[1]} | Sex: {row[2]} | Count: {row[3]} | Year: {row[4]}")

        except sqlite3.Error as e:
            print("Database error while searching name:", e)

    def update_record(self, record_id, name, sex, count, year):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE babynames
                    SET name = ?, sex = ?, count = ?, year = ?
                    WHERE id = ?
                """, (name, sex, count, year, record_id))
                conn.commit()

                if cursor.rowcount == 0:
                    print("No record found with that ID.")
                else:
                    print("Record updated successfully.")

        except sqlite3.Error as e:
            print("Database error while updating record:", e)

    def delete_record(self, record_id):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    DELETE FROM babynames
                    WHERE id = ?
                """, (record_id,))
                conn.commit()

                if cursor.rowcount == 0:
                    print("No record found with that ID.")
                else:
                    print("Record deleted successfully.")

        except sqlite3.Error as e:
            print("Database error while deleting record:", e)

    def show_sample_records(self):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, name, sex, count, year
                    FROM baby_names
                    LIMIT 20
                """)
                results = cursor.fetchall()

                if not results:
                    print("No records found.")
                    return

                print("\nSample Records:")
                for row in results:
                    print(f"ID: {row[0]} | Name: {row[1]} | Sex: {row[2]} | Count: {row[3]} | Year: {row[4]}")

        except sqlite3.Error as e:
            print("Database error while showing records:", e)
