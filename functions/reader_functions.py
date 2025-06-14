import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from datetime import datetime, timedelta
from classes.basket import Basket
from . import data_functions as df
from . import book_function as bf


def book_basket(user):
    books = df.load_books()
    baskets = df.load_baskets()

    for book in baskets:
        if book.user_id == user.user_id:
            days = (datetime.now() - book.basket_date).days
            if days > 14:
                print(f"{Fore.RED}Turite perlaikytą knygą {book.book_title}, todėl negalite imti naujų")
                return
            
    bf.list_books()

    try:
        book_title = input("Įveskite knygos pavadinimą kurią norite paimti: ")
        for book in books:
            if book.book_title == book_title:
                if book.book_unit <= 0:
                    print(f"{Fore.RED}Knygos šiuo metu nėra sandėlyje.")
                    return 
                # Patikrina ar jau turi tą knygą
                if any(book.book_title == book_title and book.user_id == user.user_id for book in baskets):
                    print(f"{Fore.RED}Jūs jau pasiskolinote šią knygą.")
                    return
                # Skolina
                book.book_unit -= 1
                new_basket = Basket(user.user_id, user.user_name, book.book_id, book.book_title)
                baskets.append(new_basket)
                df.save_books(books)
                df.save_baskets(baskets)
                print("-" * 60)
                print(f"{Fore.GREEN}Knyga {book.book_title} paimė {user.user_name} ir privalo grąžinti iki: {Fore.MAGENTA}{(datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")}")
                return
        print(f"{Fore.RED}Knyga nerasta.")
    except ValueError:
        print(f"{Fore.RED}Netinkamas ID.")
    

def return_book(user):
    baskets = df.load_baskets()
    books = df.load_books()
    user_baskets = [book for book in baskets if book.user_id == user.user_id]

    if not user_baskets:
        print(f"{Fore.GREEN}Neturite pasiskolintų knygų.")
        return

    print(f"{Fore.CYAN}Jūsų knygos:")
    for book in user_baskets:
        print(book)

    try:
        book_title = input("Įveskite knygos pavadinimą, kurią norite grąžinti: ")
        # Pašalinam iš krepšelio
        baskets = [book for book in baskets if not (book.user_id == user.user_id and book.book_title == book_title)]
        # Padidinam knygų kiekį
        for book in books:
            if book.book_title == book_title:
                book.book_unit += 1
        df.save_books(books)
        df.save_baskets(baskets)
        print(f"{Fore.BLUE}-" * 50)
        print(f"{user.user_name} grąžino {book.book_title} knygą")
    except ValueError:
        print(f"{Fore.RED}Netinkamas ID.")


def view_my_books(user):
    baskets = df.load_baskets()
    user_baskets = [book for book in baskets if book.user_id == user.user_id]
    if not user_baskets:
        print(f"{Fore.GREEN}Neturite pasiskolintų knygų.")
    else:
        print(f"{Fore.CYAN}Jūsų pasiskolintos knygos:")
        for book in user_baskets:
            print(f"{Fore.BLUE}-" * 140)
            print(book)
