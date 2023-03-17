import sqlite3
from .structures import Structures
from .sections import Sections

connection = sqlite3.connect("gmc_infrastructure.db")
cursor = connection.cursor()

structures = Structures(cursor, connection)
section = Sections(cursor, connection)