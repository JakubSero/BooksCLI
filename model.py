import datetime

class Book:
    def __init__(self, title, author, year_published, date_added):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.date_added = date_added if date_added is not None else datetime.date.today()

    def __repr__(self) -> str:
        return f"{self.title}, {self.author}, {self.year_published}, {self.date_added}"