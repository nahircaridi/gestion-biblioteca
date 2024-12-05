import sqlite3

def create_connection():
    conn = sqlite3.connect('biblioteca.db') 
    return conn
