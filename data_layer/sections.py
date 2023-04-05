from data_layer.data_models.section import Section


def fetch_all(cursor):
    def fetch_all_sections():
        cursor.execute("SELECT * FROM gmc_sections ORDER BY name ASC")
        rows = cursor.fetchall()
        sections = [Section(row) for row in rows]
        return sections
    return fetch_all_sections


def add_section(cursor, connection):
    def add_section(section):
        cursor.execute("INSERT INTO gmc_sections DEFAULT VALUES")
        connection.commit()
        return cursor.lastrowid
    return add_section

def update_section(cursor, connection):
    def update_section(section):
        data = (
            section.name,
            section.description,
            section.founded,
            section.area_of_control,
            section.id
        )
        cursor.execute("UPDATE gmc_sections SET name = ?, description = ?, founded = ?, area_of_control= ? WHERE id = ?", data)
        connection.commit()
    return update_section

def delete_section(cursor, connection):
    def delete_section(delete_id):
        my_id = str(delete_id)
        print("Deleting structure", my_id)
        cursor.execute("DELETE FROM gmc_sections WHERE id=" + my_id)
        connection.commit()

    return delete_section

class Sections:
    def __init__(self, cursor, connection):
        self.fetch_all = fetch_all(cursor)
        self.add_section = add_section(cursor, connection)
        self.update_section = update_section(cursor, connection )
        self.delete_section = delete_section(cursor, connection)






