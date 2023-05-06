import requests
from rich import print

def get_books(genre):
    headers = {'Accept': 'application/json'}

    r = requests.get("https://gutendex.com/books?topic="+ 
                     genre, headers=headers)
    
    # print(f"Start: {r.json()}")
    try:
        for _ in r.json()['results']:
            print("[bold red]Title:[/bold red]", _['title'], "[bold red]Author:[/bold red]", _['authors'][0]['name'])
    except:
        print("Something went wrong in the retrieval of this list.")

if __name__ == '__main__':
    get_books('science fiction')