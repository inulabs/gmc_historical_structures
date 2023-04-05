from data_layer.data_models.image import Image

def fetch_all_by_structure(cursor):
    def fetch_all_images(sid):
        cursor.execute("SELECT * from images JOIN structure_images si on images.id = si.image_id WHERE structure_id = ?", (sid, ))
        rows = cursor.fetchall()
        images = [Image(row) for row in rows]
        return images

    return fetch_all_images


def add_structure_image(cursor, connection):
    def add_image(structure_id, path):
        print("Adding image", path)
        cursor.execute("INSERT INTO images ('path') VALUES (?)", (path,))
        connection.commit()
        image_id = cursor.lastrowid
        cursor.execute("INSERT INTO structure_images ('structure_id', 'image_id') VALUES (?, ?)", (structure_id, image_id))
        connection.commit()
        return image_id

    return add_image

def update_image(cursor, connection):
    def update_image(image):

        data = (
            image["title"],
            image["description"],
            image["caption"],
            image["date"],
            image["path"],
            image["id"]
        )

        cursor.execute("UPDATE images SET title = ?,  description = ?, caption= ?,  date = ?,  path = ?  WHERE id = ?", data)
        connection.commit()

    return update_image


def delete_image(cursor, connection):
    def delete_image(delete_id):
        my_id = str(delete_id)
        print("Deleting image", my_id)
        connection.execute('pragma foreign_keys=ON')
        cursor.execute("DELETE FROM images WHERE id=" + my_id)
        connection.commit()

    return delete_image


class Images:
    def __init__(self, cursor, connection):
        self.fetch_all_by_structure = fetch_all_by_structure(cursor)
        self.add_structure_image = add_structure_image(cursor, connection)
        self.update_image = update_image(cursor, connection)
        self.delete_image = delete_image(cursor, connection)
