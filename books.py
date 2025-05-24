from data import books, create_book

def add_book():
    """Dodaje nową książkę do biblioteki"""
    author = input("Podaj autora: ")
    title = input("Podaj tytuł: ")
    year = input("Podaj rok wydania: ")
    pages = input("Podaj liczbę stron: ")
    copies = input("Podaj ilość egzemplarzy: ")
    books.append(create_book(author, title, int(year), int(pages), int(copies)))
    print("Dodano książkę!")

def edit_book():
    """Edytuje istniejącą książkę"""
    if not books:
        print("Brak książek w bibliotece!")
        return
        
    for i, book in enumerate(books):
        print(f"{i+1}. {book['title']} by {book['author']}")
    
    try:
        idx = int(input("Którą książkę chcesz edytować? (podaj numer) ")) - 1
        if 0 <= idx < len(books):
            print("Pozostaw puste, by nie zmieniać:")
            author = input(f"Nowy autor [obecnie: {books[idx]['author']}]: ") or books[idx]['author']
            title = input(f"Nowy tytuł [obecnie: {books[idx]['title']}]: ") or books[idx]['title']
            year = input(f"Nowy rok [obecnie: {books[idx]['year']}]: ") or books[idx]['year']
            pages = input(f"Nowa liczba stron [obecnie: {books[idx]['pages']}]: ") or books[idx]['pages']
            copies = input(f"Nowa liczba egzemplarzy [obecnie: {books[idx]['copies']}]: ") or books[idx]['copies']
            books[idx] = create_book(author, title, int(year), int(pages), int(copies))
            print("Zaktualizowano książkę!")
        else:
            print("Błędny numer książki.")
    except ValueError:
        print("Podaj prawidłowy numer!")

def remove_book():
    """Usuwa książkę z biblioteki"""
    if not books:
        print("Brak książek w bibliotece!")
        return
        
    for i, book in enumerate(books):
        print(f"{i+1}. {book['title']} by {book['author']}")
    
    try:
        idx = int(input("Którą książkę usunąć? (podaj numer): ")) - 1
        if 0 <= idx < len(books):
            books.pop(idx)
            print("Usunięto książkę.")
        else:
            print("Zły numer!")
    except ValueError:
        print("Podaj prawidłowy numer!")

def show_books():
    """Wyświetla wszystkie książki"""
    print("\n=== WSZYSTKIE KSIĄŻKI ===")
    if not books:
        print("Brak książek w bibliotece.")
        return
    
    for i, book in enumerate(books):
        available = book['copies'] - book['borrowed']
        status = f"dostępne: {available}/{book['copies']}"
        print(f"{i+1}. '{book['title']}' - {book['author']} ({book['year']}) - {status}")