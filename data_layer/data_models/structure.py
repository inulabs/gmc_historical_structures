from dataclasses import dataclass

@dataclass
class Structure:
    id: int
    name: str
    type: str
    description: str
    built_date: str
    removal_date: str
    latitude: float
    longitude: float
    division: str
    section: str
    elevation: float
    location: str

    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.type = row[2]
        self.description = row[3]
        self.built_date = row[4]
        self.removal_date = row[5]
        self.latitude = row[6]
        self.longitude = row[7]
        self.division = row[8]
        self.section = row[9]
        self.elevation = row[10]
        self.location = row[11]

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type,
            'built_date': self.built_date,
            'removal_date': self.removal_date,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'division': self.division,
            'section': self.section,
            'elevation': self.elevation,
            'location': self.location
        }

