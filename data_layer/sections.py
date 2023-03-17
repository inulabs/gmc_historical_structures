import sqlite3
from models.section import Section


def fetch_all(cursor):
    def fetch_all_sections():
        cursor.execute("SELECT * FROM sections")
        rows = cursor.fetchall()
        sections = [Section(row) for row in rows]
        return sections
    return fetch_all_sections


def add_section(cursor, connection ):
    def add_section(section):
        cursor.execute("INSERT INTO sections VALUES (?,?,?,?,?,?,?,?,?,?)", section)
        connection.commit()
    return add_section

def update_section(cursor, connection):
    def update_section(section):
        cursor.execute("UPDATE sections SET name = ?, type = ?, description = ?, build_date = ?, removed_date = ?, latitude = ?, longitude = ?, division = ?, section = ? WHERE id = ?", section)
        connection.commit()
    return update_section

def delete_section(cursor, connection):
    def delete_section(section):
        cursor.execute("DELETE FROM sections WHERE id = ?", section)
        connection.commit()
    return delete_section

class Sections:
    def __init__(self, cursor, connection):
        self.fetch_all = fetch_all(cursor)
        self.add_section = add_section(cursor, connection)
        self.update_section = update_section(cursor, connection )
        self.delete_section = delete_section(cursor, connection)






