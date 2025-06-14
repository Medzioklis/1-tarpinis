import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from classes.book import Book
from . import data_functions as df

def add_book():
    books = df.load_books()
    book_id = df.get_id()
    book_title = input("Įveskite knygos pavadinimą: ")
    book_author = input("Įveskite autorių: ")
    while True:
        book_genre = input("Įveskite knygos žanrą:(romanas, detektyvas, fantastika, biografija): ").lower()
        if book_genre == "detektyvas" or book_genre == "romanas" or book_genre == "fantastika" or book_genre == "biografija":
            break
        else:
            print(f"{Fore.RED}Neteisingai įvedėte {book_genre} žanrą. Bandykite dar kartą")
    book_release = input("Įveskite išleidimo metus: ")
    try:
        book_unit = int(input("Įveskite kiekį (kiek egzempliorių): "))
    except ValueError:
        print(f"{Fore.RED}Kiekis turi būti sveikas skaičius.")
        return
    book = Book(book_id, book_title, book_author, book_genre, book_release, book_unit)
    books.append(book)
    df.save_books(books)
    print(f"{Fore.BLUE}-" * 140)
    print(f"Knygos ID: {book.book_id}, pavadinimas: {book.book_title}, autorius: {book.book_author}, žanras: {book.book_genre}, leidinio metai: {book.book_release}, sandelyje: {book.book_unit} vnt.")


def delete_book():
    books = df.load_books()
    original_len = len(books)
    book_id = input("Įveskite knygos ID, kurią norite ištrinti: ")
    books = [book for book in books if book.book_id != book_id]
    if len(books) < original_len:                               # tikrinam ar saraso ilgis sumazejo, jei sumazejo reiskia kad knyga istrinta ir galima is naujo isaugoti sarasa
        df.save_books(books)
        print("-" * 60)
        print(f"{Fore.GREEN}Knyga su ID: {book_id} ištrinta")
    else:
        print("-" * 60)
        print(f"{Fore.RED}Knyga su ID: {book_id} nerasta")


def update_book():
    books = df.load_books()
    try:
        book_id = input("Įveskite knygos ID, kurią norite atnaujinti: ")
        for book in books:
            if book.book_id == book_id:
                book_title = input(f"Naujas pavadinimas (dabar:{Fore.RED} {book.book_title}): ")
                if book_title and book_title != book.book_title:
                    book.book_title = book_title
                book_author = input(f"Naujas autorius (dabar{Fore.RED} {book.book_author}): ")
                if book_author:
                    book.book_author = book_author
                while True:
                    book_genre = input(f"Naujas žanras (dabar: {Fore.RED}{book.book_genre}): ").lower()
                    if book_genre == "detektyvas" or book_genre == "romanas" or book_genre == "fantastika" or book_genre == "biografija" or book_genre == "":
                        break
                    else:
                        print(f"{Fore.RED}Neteisingai įvedėte {book_genre} žanrą. Bandykite dar kartą")
                book_release = input(f"Nauji išleidimo metai (dabar: {Fore.RED}{book.book_release}): ")
                if book_release:
                    book.book_release = book_release
                while True:
                    try:
                        book_unit = int(input(f"Atnaujinkite vnt., skaičių (privaloma) (dabar yra: {Fore.RED}{book.book_unit} vnt.): "))
                        if book_unit:
                            book.book_unit = book_unit
                        break
                    except ValueError:
                        print(f"{Fore.RED}Įveskite vienetų skaičių")
                df.save_books(books)
                print("_" * 140)
                print(f"{Fore.GREEN}Atnaujintos knygos ID: {book.book_id}, pavadinimas: {book.book_title}, autorius: {book.book_author}, žanras: {book.book_genre}, leidinio metai: {book.book_release}, sandelyje: {book.book_unit} vnt.")
                return
        print(f"{Fore.RED}Knyga nerasta.")
    except ValueError:
        print(f"{Fore.RED}Netinkamas ID formatas.")


def search_books():
    books = df.load_books()
    search_input = input("Ieškokite pagal knygos pavadinimą arba autorių: ").lower()
    results = [book for book in books if search_input in book.book_title.lower() or search_input in book.book_author.lower()]
    if results:
        for book in results:
            print(f"{Fore.BLUE}-" * 140)
            print(book)
            print(f"{Fore.BLUE}-" * 140)
    else:
        print(f"{Fore.RED}Knygų nerasta.")


def list_books():
    books = df.load_books()
    if not books:
        print(f"{Fore.RED}Knygų sąrašas tuščias.")
    else:
        for book in books:
            print(f"{Fore.BLUE}-" * 140)
            print(book)
            print(f"{Fore.BLUE}-" * 140)