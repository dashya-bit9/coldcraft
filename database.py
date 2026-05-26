import sqlite3
from datetime import date


def init_db():
    conn = sqlite3.connect("coldcraft.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drafts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            industry TEXT,
            tone TEXT,
            bullets TEXT,
            generated_email TEXT,
            date TEXT
        )       
    """)

    conn.commit()
    conn.close()


def save_draft(industry, tone, bullets, generated_email):
    conn = sqlite3.connect("coldcraft.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO drafts (industry, tone, bullets, generated_email, date)
        VALUES (?, ?, ?, ?, ?)
    """, (industry, tone, bullets, generated_email, str(date.today())))

    conn.commit()
    conn.close()


def get_drafts():
    conn = sqlite3.connect("coldcraft.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, industry, tone, generated_email, date
        FROM drafts
        ORDER BY id DESC
    """)

    drafts = cursor.fetchall()
    conn.close()

    return drafts