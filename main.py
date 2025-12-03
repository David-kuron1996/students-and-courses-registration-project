from database import init_db
from student import add_student, update_student, delete_student, list_students
from course import add_course, update_course, delete_course, list_courses
from utils import display_menu, get_user_input

def main():
    # Initialize the database
    init_db()
    
    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-9): ", int)
        
        if choice == 1:  # Add Student
            print("\nAdd New Student")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            phone = input("Enter student phone (optional): ") or None
            address = input("Enter student address (optional): ") or None
            add_student(name, email, phone, address)