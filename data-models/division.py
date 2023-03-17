from dataclasses import dataclass

@dataclass
class Division:
    id: int
    description: str
    division_number: int
    mileage: float
    section_id: int

    def __init__(self, row):
        self.id = row[0]
        self.description = row[1]
        self.division_number = row[2]
        self.mileage = row[3]
        self.section_id = row[4]



