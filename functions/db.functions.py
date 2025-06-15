import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import sqlite3
from datetime import datetime


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file) 
        print(f"{Fore.GREEN}Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(f"{Fore.RED}Error connecting to database: {e}")
    return conn

db_file = r"data\library_db.db"
current_patch = os.path.dirname(os.path.abspath(__file__))
full_patch = os.path.join(current_patch, db_file)


conn = create_connection(full_patch)
cursor = conn.cursor()

with conn:
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(255), password varchar(30), role varchar(30) )')

conn.close()