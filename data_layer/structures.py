from data_layer.data_models.structure import Structure

def fetch_all(cursor):
    def fetch_all_structures():
        cursor.execute("SELECT * FROM structures")
        rows = cursor.fetchall()
        structures = [Structure(row) for row in rows]
        return structures

    return fetch_all_structures


def add_structure(cursor, connection):
    def add_structure():
        cursor.execute("INSERT INTO structures DEFAULT VALUES")
        connection.commit()
        return cursor.lastrowid

    return add_structure


def update_structure(cursor, connection):
    def update_structure(structure):
        data = (
            structure.name,
            structure.type,
            structure.description,
            structure.built_date,
            structure.removal_date,
            structure.latitude,
            structure.longitude,
            structure.division,
            structure.section,
            structure.elevation,
            structure.location,
            structure.id
        )

        cursor.execute(
            "UPDATE structures SET name = ?,  type = ?, description = ?,  built_date = ?,  removal_date = ?,  latitude = ?,  longitude = ?,  division = ?, section = ?,  elevation = ?, location = ? WHERE id = ?",
            data)
        connection.commit()

    return update_structure


def delete_structure(cursor, connection):
    def delete_structure(delete_id):
        my_id = str(delete_id)
        print("Deleting structure", my_id)
        cursor.execute("DELETE FROM structures WHERE id=" + my_id)
        connection.commit()

    return delete_structure


class Structures:
    def __init__(self, cursor, connection):
        self.fetch_all = fetch_all(cursor)
        self.add_structure = add_structure(cursor, connection)
        self.update_structure = update_structure(cursor, connection)
        self.delete_structure = delete_structure(cursor, connection)
