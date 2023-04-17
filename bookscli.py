import typer
import pyfiglet
from rich.console import Console
from rich.table import Table
from model import Book

# from rich import print

app = typer.Typer()
console = Console()
out = pyfiglet.figlet_format("My Books!", font='doom')


@app.command()
def home():
    print('\n' * 150)
    print(out)
    table = Table("Command", "Description")
    print("Get Started Here!")
    print('---------')
    table.add_row("login", "enter your name to identify yourself")
    table.add_row("add", "add a book to your book list by title")
    table.add_row("my-books", "opens your read book list")
    console.print(table)
    print('---------')
    table2 = Table("Command", "Description")
    table2.add_row("remove", "remove a book from your book list by title")
    table2.add_row("to-read", "view the list of books you want to read")
    table2.add_row("add-to-read", "add a book to your To Read list")
    table2.add_row("remove-to-read", "remove a book from your To Read list")
    table2.add_row("popular", "type a genre and find out more about the most popular books")
    table2.add_row("botd", "displays the random book of the day with some information")
    console.print(table2)


@app.command(short_help='add a book to your book list by title')
def add(title: str = typer.Option(..., prompt=True),
        author: str = typer.Option(..., prompt=True),
        year_published: str = typer.Option(..., prompt=True)):
    book = Book(title, author, year_published, date_added=None)
    console.print(book)
    console.print(f"Adding {title} by {author}, published in {year_published}.")


@app.command(short_help='remove a book from your book list by title')
def remove(title: str = typer.Option(..., prompt=True, confirmation_prompt=True)):
    console.print(f"Removing {title}")


@app.command(short_help='view the list of books you want to read')
def to_read():
    console.print(f"Opening to-read list")


@app.command(short_help='enter a title to add it to your To Read list')
def add_to_read(title: str = typer.Option(..., prompt=True),
                author: str = typer.Option(..., prompt=True),
                year_published: str = typer.Option(..., prompt=True)):
    book = Book(title, author, year_published, date_added=None)
    console.print(f"Adding {title} by {author} to your To-Read list, published in {year_published}.")


@app.command(short_help='enter a title to add it to your To Read list')
def remove_to_read(title: str = typer.Option(..., prompt=True, confirmation_prompt=True)):
    console.print(f"Removing {title} from your To Read list")


@app.command(short_help='type a genre and find out more about the most popular books')
def popular(genre: str):
    console.print(f"Displaying most popular {genre} books")


@app.command(short_help='type a name to identify yourself to the database')
def login(name: str = typer.Option(..., prompt=True)):
    console.print(f"Welcome {name}")


@app.command(short_help='opens your read book list')
def my_books():
    console.print(f"Opening my book list")


@app.command(short_help='displays the random book of the day with some information')
def botd():
    console.print(f"Here is the book of the day:")

def show():
    pass


if __name__ == '__main__':
    app()
