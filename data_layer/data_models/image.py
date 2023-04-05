from dataclasses import dataclass

@dataclass
class Image:
    id: int
    title: str
    description: str
    path: str
    caption: str
    date: str


    def __init__(self, row):
        self.id = row[0]
        self.title = row[1]
        self.description = row[2]
        self.caption = row[3]
        self.date = row[4]
        self.path = row[5]


    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'caption': self.caption,
            'date': self.date,
            'path': self.path
        }

