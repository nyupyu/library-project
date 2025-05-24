# Globalna listy danych
books = []
students = []

# Stałe konfiguracyjne
MAX_BOOKS_PER_STUDENT = 5
MAX_STUDENTS = 15

def create_book(author, title, year, pages, copies):
    """Tworzy słownik reprezentujący książkę"""
    return {
        'author': author,
        'title': title,
        'year': year,
        'pages': pages,
        'copies': copies,
        'borrowed': 0 
    }

def create_student(name):
    """Tworzy słownik reprezentujący studenta"""
    return {
        'name': name,
        'borrowed_books': []
    }

def find_student(name):
    """Znajduje studenta po imieniu i nazwisku"""
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None

def find_book(title):
    """Znajduje książkę po tytule"""
    for book in books:
        if book['title'].lower() == title.lower():
            return book
    return None