from dataclasses import dataclass

@dataclass
class Structure:
    id: int
    name: str
    type: str
    description: str
    build_date: str
    removed_date: str
    latitude: float
    longitude: float
    division: str
    section: str

    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.type = row[2]
        self.description = row[3]
        self.build_date = row[4]
        self.removed_date = row[5]
        self.latitude = row[6]
        self.longitude = row[7]
        self.division = row[8]
        self.section = row[9]


