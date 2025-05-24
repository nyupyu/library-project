from books import add_book, edit_book, remove_book, show_books
from students import add_student, show_students
from borrowing import borrow_book, return_book, show_borrowed_books_report

def show_menu():
    """Wyświetla menu główne"""
    print("\n" + "="*40)
    print("           SYSTEM BIBLIOTEKI")
    print("="*40)
    print("1. Dodaj książkę")
    print("2. Edytuj książkę")
    print("3. Usuń książkę")
    print("4. Pokaż wszystkie książki")
    print("5. Dodaj studenta")
    print("6. Pokaż studentów")
    print("7. Wypożycz książkę")
    print("8. Zwróć książkę")
    print("9. Raport wypożyczeń")
    print("0. Wyjście")
    print("="*40)

def handle_menu_choice(choice):
    """Obsługuje wybór z menu"""
    if choice == '1':
        add_book()
    elif choice == '2':
        edit_book()
    elif choice == '3':
        remove_book()
    elif choice == '4':
        show_books()
    elif choice == '5':
        add_student()
    elif choice == '6':
        show_students()
    elif choice == '7':
        borrow_book()
    elif choice == '8':
        return_book()
    elif choice == '9':
        show_borrowed_books_report()
    elif choice == '0':
        return False  # Sygnał do zakończenia
    else:
        print("Nieprawidłowa opcja!")
    
    return True