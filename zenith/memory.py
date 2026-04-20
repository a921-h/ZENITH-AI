import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = "zenith_memory.sqlite"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            relevance INTEGER DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            type TEXT,
            description TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relationships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id INTEGER,
            target_id INTEGER,
            relation TEXT,
            FOREIGN KEY(source_id) REFERENCES entities(id),
            FOREIGN KEY(target_id) REFERENCES entities(id)
        )
    """)
    conn.commit()
    conn.close()

def save_insight(content: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO insights (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

def get_recent_insights(limit=5):
    if not os.path.exists(DB_PATH):
        return ""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM insights ORDER BY created_at DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return "\n".join([f"- {r[0]}" for r in rows])

def save_entity(name: str, entity_type: str, description: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO entities (name, type, description)
        VALUES (?, ?, ?)
    """, (name, entity_type, description))
    conn.commit()
    conn.close()

def save_relationship(source_name: str, target_name: str, relation: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Get IDs
    cursor.execute("SELECT id FROM entities WHERE name = ?", (source_name,))
    source = cursor.fetchone()
    cursor.execute("SELECT id FROM entities WHERE name = ?", (target_name,))
    target = cursor.fetchone()
    
    if source and target:
        cursor.execute("""
            INSERT INTO relationships (source_id, target_id, relation)
            VALUES (?, ?, ?)
        """, (source[0], target[0], relation))
    conn.commit()
    conn.close()

def get_knowledge_graph():
    if not os.path.exists(DB_PATH):
        return ""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e1.name, r.relation, e2.name 
        FROM relationships r
        JOIN entities e1 ON r.source_id = e1.id
        JOIN entities e2 ON r.target_id = e2.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return "\n".join([f"- {r[0]} {r[1]} {r[2]}" for r in rows])

def delete_old_insights():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM insights WHERE created_at < ?", (datetime.now() - timedelta(days=30),))
    conn.commit()
    conn.close()