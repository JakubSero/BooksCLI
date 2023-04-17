import datetime


class Book:
    def __init__(self, title, author, year_published, date_added=None, position=None):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.date_added = date_added if date_added is not None else datetime.date.today()
        self.position = position if position is not None else None

    def __repr__(self) -> str:
        return f"{self.title}, {self.author}, {self.year_published}, {self.date_added}, {self.position}"
