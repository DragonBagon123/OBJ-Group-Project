import sqlite3
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

def get_db():
    return sqlite3.connect("babynames.db")


@app.get("/")
def home():
    return {"message": "Baby Name API is running"}


@app.get("/nameinfo")
def name_info(name: str = Query(None)):

    if not name:
        return JSONResponse(
            status_code=400,
            content={"error": "Missing name parameter"}
        )

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT year, count
        FROM names
        WHERE lower(name)=lower(?)
        ORDER BY year
    """, (name,))

    rows = cursor.fetchall()

    if not rows:
        conn.close()
        return JSONResponse(
            status_code=404,
            content={"error": "Name not found"}
        )

    first_year = rows[0][0]

    most_popular_year = max(rows, key=lambda x: x[1])[0]

    top_10 = sorted(rows, key=lambda x: x[1], reverse=True)[:10]
    top_years = [row[0] for row in top_10]

    estimated_age = 2026 - most_popular_year

    conn.close()

    return {
        "name": name.title(),
        "estimated_age": estimated_age,
        "first_year": first_year,
        "most_popular_year": most_popular_year,
        "top_10_years": top_years
    }
