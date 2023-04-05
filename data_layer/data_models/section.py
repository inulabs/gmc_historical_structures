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

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'founded': self.founded,
            'area_of_control': self.area_of_control
        }



