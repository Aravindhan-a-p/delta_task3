import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")

cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS userdata (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
    )
"""
)
            
username1, password1 = "interstellar", hashlib.sha256("mathew@23".encode()).hexdigest()
username2, password2 = "inception", hashlib.sha256("leo@25".encode()).hexdigest()
username3, password3 = "dunkirk", hashlib.sha256("ww1@1914".encode()).hexdigest()
username4, password4 = "darkknight", hashlib.sha256("joker@69".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username1,password1))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username2,password2))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username3,password3))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username4,password4))

conn.commit()