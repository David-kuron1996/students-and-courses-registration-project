from database import init_db
from student import add_student, update_student, delete_student, list_students
from course import add_course, update_course, delete_course, list_courses
from main import display_menu, get_user_input

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

        elif choice == 3:  # Delete Student
            list_students()
            student_id = get_user_input("\nEnter student ID to delete: ", int)
            confirm = input(f"Are you sure you want to delete student with ID {student_id}? (y/n): ").lower()
            if confirm == 'y':
                delete_student(student_id)
            else:
                print("Deletion cancelled.")
                
        elif choice == 4:  # List Students
            list_students()
            
        elif choice == 5:  # Add Course
            print("\nAdd New Course")
            name = input("Enter course name: ")
            code = input("Enter course code: ")
            description = input("Enter course description (optional): ") or None
            add_course(name, code, description) 
            
        elif choice == 6:  # Update Course
            list_courses()
            course_id = get_user_input("\nEnter course ID to update: ", int)
            print("\nLeave blank to keep current value")
            
            name = input("Enter new name (current: ").strip() or None
            code = input("Enter new code (current: ").strip() or None
            description = input("Enter new description (current: ").strip() or None
            
            update_course(course_id, name, code, description)
            
        elif choice == 7:  # Delete Course
            list_courses()
            course_id = get_user_input("\nEnter course ID to delete: ", int)
            confirm = input(f"Are you sure you want to delete course with ID {course_id}? (y/n): ").lower()
            if confirm == 'y':
                delete_course(course_id)
            else:
                print("Deletion cancelled.")

       
        
        elif choice == 8:  # List Courses
            list_courses()

        elif choice == 9:  # Exit
            print("Thank you for using the Students Registration System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()    
                   
            