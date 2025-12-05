# debug.py
from database import init_db
from student import add_student, update_student, delete_student, list_students
from course import add_course, update_course, delete_course, list_courses
from enrollment import add_enrollment, remove_enrollment, list_enrollments
from main import display_menu, get_user_input

def main():
    # Initialize the database
    init_db()
    
    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-12): ", int)
        
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
            student = None
            # Get current student data
            from database import get_db_connection, Student
            session = get_db_connection()
            try:
                student = session.query(Student).filter_by(id=student_id).first()
                if not student:
                    print(f"Student with ID {student_id} not found.")
                    continue
            finally:
                session.close()
            
            print("\nLeave blank to keep current value")
            name = input(f"Enter new name (current: {student.name}): ").strip() or None
            email = input(f"Enter new email (current: {student.email}): ").strip() or None
            phone = input(f"Enter new phone (current: {student.phone or 'N/A'}): ").strip() or None
            address = input(f"Enter new address (current: {student.address or 'N/A'}): ").strip() or None
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
            course = None
            # Get current course data
            from database import get_db_connection, Course
            session = get_db_connection()
            try:
                course = session.query(Course).filter_by(id=course_id).first()
                if not course:
                    print(f"Course with ID {course_id} not found.")
                    continue
            finally:
                session.close()
            
            print("\nLeave blank to keep current value")
            name = input(f"Enter new name (current: {course.name}): ").strip() or None
            code = input(f"Enter new code (current: {course.code}): ").strip() or None
            description = input(f"Enter new description (current: {course.description or 'N/A'}): ").strip() or None
            
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
            
        elif choice == 9:  # List Enrollments
            list_enrollments()
            
        elif choice == 10:  # Add Enrollment
            list_students()
            student_id = get_user_input("\nEnter student ID to enroll: ", int)
            
            list_courses()
            course_id = get_user_input("\nEnter course ID to enroll in: ", int)
            
            add_enrollment(student_id, course_id)
            
        elif choice == 11:  # Remove Enrollment
            list_enrollments()
            enrollment_id = get_user_input("\nEnter enrollment ID to remove: ", int)
            
            confirm = input(f"Are you sure you want to remove this enrollment? (y/n): ").lower()
            if confirm == 'y':
                remove_enrollment(enrollment_id)
            else:
                print("Removal cancelled.")
                
        elif choice == 12:  # Exit
            print("Thank you for using the Students Registration System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()