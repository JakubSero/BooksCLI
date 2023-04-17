import sqlite3
from typing import List
import datetime
from model import Book

conn = sqlite3.connect('books.db')
c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Books (
            title text NOT NULL,
            author text NOT NULL,
            year_published integer NOT NULL,
            date_added text,
            position integer);  
            """)


def add_book(book: Book):
    c.execute("SELECT count(*) FROM Books")
    count = c.fetchone()[0]
    book.position = count if count else 0
    with conn:
        c.execute("INSERT INTO Books VALUES (:title, :author, :year_published, :date_added, :position)",
                  {'title': book.title, 'author': book.author, 'year_published': book.year_published,
                   'date_added': book.date_added, 'position': book.position})


def get_all_books() -> List[Book]:
    c.execute("SELECT * FROM Books")
    results = c.fetchall()
    books = []
    for result in results:
        books.append(Book(*result))
    return books


def delete_book(title):
    position = get_pos(title)

    c.execute("SELECT count(*) FROM Books")
    count = c.fetchone()[0]

    with conn:
        c.execute("DELETE FROM Books WHERE title=:title", {"title": title})
        for pos in range(position + 1, count):
            change_position(pos, pos - 1, False)


def get_pos(title):
    c.execute("SELECT position FROM Books WHERE title=:title", {"title": title})
    results = c.fetchall()
    pos = []
    for result in results:
        pos.append(result)
    return pos[0][0]


def change_position(old_pos, new_pos, commit=True):
    c.execute("UPDATE Books SET position = :new_pos WHERE position =:old_pos",
              {'new_pos': new_pos, 'old_pos': old_pos})
    if commit:
        conn.commit()


if __name__ == '__main__':
    create_table()
