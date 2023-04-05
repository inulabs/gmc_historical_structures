import sqlite3
from .structures import Structures
from .sections import Sections
from .images import Images

connection = sqlite3.connect("gmc_infrastructure.db")
cursor = connection.cursor()

structures = Structures(cursor, connection)
sections = Sections(cursor, connection)
images = Images(cursor, connection)