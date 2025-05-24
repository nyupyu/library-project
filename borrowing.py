from data import books, students, find_student, find_book, MAX_BOOKS_PER_STUDENT

def borrow_book():
    """Wypożycza książkę studentowi"""
    if not books:
        print("Brak książek w bibliotece!")
        return
    if not students:
        print("Brak studentów w systemie!")
        return
    
    print("\n=== DOSTĘPNE KSIĄŻKI ===")
    available_books = []
    for i, book in enumerate(books):
        if book['copies'] > book['borrowed']:
            available_books.append(book)
            print(f"{len(available_books)}. '{book['title']}' - {book['author']} (dostępne: {book['copies'] - book['borrowed']})")
    
    if not available_books:
        print("Brak dostępnych książek!")
        return
    
    try:
        book_choice = int(input("Wybierz numer książki: ")) - 1
        chosen_book = available_books[book_choice]
        
        student_name = input("Podaj imię i nazwisko studenta: ")
        student = find_student(student_name)
        
        if not student:
            print("Student nie znaleziony!")
            return
        
        if len(student['borrowed_books']) >= MAX_BOOKS_PER_STUDENT:
            print(f"Student ma już wypożyczone maksymalnie {MAX_BOOKS_PER_STUDENT} książek!")
            return
        
        # Wypożycz książkę
        chosen_book['borrowed'] += 1
        student['borrowed_books'].append(chosen_book['title'])
        print(f"Wypożyczono '{chosen_book['title']}' studentowi {student['name']}")
        
    except (ValueError, IndexError):
        print("Błędny wybór!")

def return_book():
    """Zwraca książkę od studenta"""
    student_name = input("Podaj imię i nazwisko studenta: ")
    student = find_student(student_name)
    
    if not student:
        print("Student nie znaleziony!")
        return
    
    if not student['borrowed_books']:
        print("Student nie ma wypożyczonych książek!")
        return
    
    print(f"\n=== WYPOŻYCZONE KSIĄŻKI - {student['name']} ===")
    for i, book_title in enumerate(student['borrowed_books']):
        print(f"{i+1}. {book_title}")
    
    try:
        book_choice = int(input("Wybierz numer książki do zwrotu: ")) - 1
        book_title = student['borrowed_books'][book_choice]
        
        # Zwróć książkę
        book = find_book(book_title)
        if book:
            book['borrowed'] -= 1
        student['borrowed_books'].remove(book_title)
        print(f"Zwrócono '{book_title}'")
        
    except (ValueError, IndexError):
        print("Błędny wybór!")

def show_borrowed_books_report():
    """Wyświetla raport wypożyczonych książek"""
    print("\n" + "="*50)
    print("         RAPORT WYPOŻYCZONYCH KSIĄŻEK")
    print("="*50)
    
    if not students:
        print("Brak studentów w systemie.")
        return
    
    has_borrowed = False
    for student in students:
        if student['borrowed_books']:
            has_borrowed = True
            print(f"\n📚 {student['name']}:")
            for book_title in student['borrowed_books']:
                print(f"   - {book_title}")
            print(f"   RAZEM: {len(student['borrowed_books'])}/5 książek")
            
            if len(student['borrowed_books']) >= 4:
                print("   ⚠️  UWAGA: Blisko limitu wypożyczeń!")
    
    if not has_borrowed:
        print("✅ Żaden student nie ma obecnie wypożyczonych książek.")
    
    print("="*50)