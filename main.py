from database import init_db
from student import add_student, update_student, delete_student, list_students
from course import add_course, update_course, delete_course, list_courses
from debug import display_menu, get_user_input

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

        elif choice == 2:  # Update Student
            list_students()
            student_id = get_user_input("\nEnter student ID to update: ", int)
            print("\nLeave blank to keep current value")
            
            name = input("Enter new name (current: ").strip() or None
            email = input("Enter new email (current: ").strip() or None
            phone = input("Enter new phone (current: ").strip() or None
            address = input("Enter new address (current: ").strip() or None
            
            update_student(student_id, name, email, phone, address)
            