import sqlite3
import os
from datetime import datetime

DB = "/app/data/notes.db"  # Absolute path, safe inside Docker

def init_db():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # Return dicts instead of tuples
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS folders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        created_at TEXT,
        updated_at TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folder_id INTEGER NOT NULL,
        title TEXT,
        content TEXT,
        created_at TEXT,
        updated_at TEXT,
        FOREIGN KEY (folder_id) REFERENCES folders(id)
    )
    """)

    conn.commit()
    conn.close()

def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # Every connection returns dicts
    return conn

def create_folder(name, description=None):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO folders (name, description, created_at, updated_at)
        VALUES (?, ?, ?, ?)
    """, (name, description, datetime.now().isoformat(), datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_folders():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM folders")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def create_note(folder_id, title, content):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO notes (folder_id, title, content, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
    """, (folder_id, title, content, datetime.now().isoformat(), datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_notes():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_notes_by_folder(folder_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE folder_id=?", (folder_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]