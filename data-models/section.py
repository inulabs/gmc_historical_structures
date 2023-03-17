from dataclasses import dataclass

@dataclass
class Section:
    id: int
    name: str
    founded: str
    description: str
    area_of_control: str

    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.founded = row[2]
        self.description = row[3]
        self.area_of_control = row[4]




