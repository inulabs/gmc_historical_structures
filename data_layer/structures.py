from data_layer.data_models.structure import Structure

def fetch_all(cursor):
    def fetch_all_structures():
        cursor.execute("SELECT * FROM structures")
        rows = cursor.fetchall()
        structures = [Structure(row) for row in rows]
        return structures

    return fetch_all_structures


def add_structure(cursor, connection):
    def add_structure(structure):
        cursor.execute("INSERT INTO structures VALUES (structure.name,?,?,?,?,?,?,?,?,?)", structure)
        connection.commit()

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
            structure.id
        )

        print(repr(data))

        cursor.execute(
            "UPDATE structures SET name = ?, type = ?, description = ?, built_date = ?, removal_date = ?, latitude = ?, longitude = ?, division = ?, section = ? WHERE id = ?",
            data)
        connection.commit()

    return update_structure


def delete_structure(cursor, connection):
    def delete_structure(structure):
        cursor.execute("DELETE FROM structures WHERE id = ?", structure)
        connection.commit()

    return delete_structure


class Structures:
    def __init__(self, cursor, connection):
        self.fetch_all = fetch_all(cursor)
        self.add_structure = add_structure(cursor, connection)
        self.update_structure = update_structure(cursor, connection)
        self.delete_structure = delete_structure(cursor, connection)
