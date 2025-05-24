from data import students, create_student, MAX_STUDENTS

def add_student():
    """Dodaje nowego studenta"""
    if len(students) >= MAX_STUDENTS:
        print("Osiągnięto maksymalną liczbę studentów (15)!")
        return
    name = input("Podaj imię i nazwisko studenta: ")
    students.append(create_student(name))
    print("Dodano studenta!")

def show_students():
    """Wyświetla wszystkich studentów"""
    if not students:
        print("Brak studentów w systemie.")
        return
    for i, student in enumerate(students):
        borrowed_count = len(student['borrowed_books'])
        print(f"{i+1}. {student['name']} - wypożyczonych książek: {borrowed_count}/5")