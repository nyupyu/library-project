from data import books, create_book
from menu import show_menu, handle_menu_choice

def initialize_sample_data():
    """Dodaje przykładowe książki na start"""
    books.extend([
        create_book("Adam Mickiewicz", "Pan Tadeusz", 1834, 350, 3),
        create_book("Henryk Sienkiewicz", "Krzyżacy", 1900, 450, 2),
        create_book("J.K. Rowling", "Harry Potter i Kamień Filozoficzny", 1997, 320, 5)
    ])

def main():
    """Główna funkcja programu"""
    initialize_sample_data()
    
    while True:
        show_menu()
        try:
            choice = input("Wybierz opcję: ")
            
            if not handle_menu_choice(choice):
                print("Dziękuję za korzystanie z systemu biblioteki!")
                break
                
        except KeyboardInterrupt:
            print("\nProgram przerwany. Miłego dnia!")
            break
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()