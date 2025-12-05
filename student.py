from database import get_db_connection, Student

def add_student(name, email, phone=None, address=None):
    """Add a new student to the database."""
    session = get_db_connection()
    
    try:
        # Check if student with this email already exists
        existing_student = session.query(Student).filter_by(email=email).first()
        if existing_student:
            print("Error: A student with this email already exists.")
            return False
            
        new_student = Student(name=name, email=email, phone=phone, address=address)
        session.add(new_student)
        session.commit()
        print(f"Student {name} added successfully!")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error adding student: {e}")
        return False
    finally:
        session.close()

def update_student(student_id, name=None, email=None, phone=None, address=None):
    """Update student information."""
    session = get_db_connection()
    
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            print(f"Student with ID {student_id} not found.")
            return False
            
        # Check if email is being updated and if it's already used by another student
        if email and email != student.email:
            existing_student = session.query(Student).filter_by(email=email).first()
            if existing_student:
                print("Error: A student with this email already exists.")
                return False
        
        # Update fields if provided
        if name:
            student.name = name
        if email:
            student.email = email
        if phone:
            student.phone = phone
        if address:
            student.address = address
            
        session.commit()
        print(f"Student with ID {student_id} updated successfully!")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error updating student: {e}")
        return False
    finally:
        session.close()

def delete_student(student_id):
    """Delete a student from the database."""
    session = get_db_connection()
    
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            print(f"Student with ID {student_id} not found.")
            return False
            
        session.delete(student)
        session.commit()
        print(f"Student with ID {student_id} deleted successfully!")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error deleting student: {e}")
        return False
    finally:
        session.close()

def list_students():
    """List all students in the database."""
    session = get_db_connection()
    
    try:
        students = session.query(Student).all()
        
        if students:
            print("\nList of Students:")
            print("=" * 50)
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}, Phone: {student.phone}, Address: {student.address}, Created At: {student.created_at}")
            print("=" * 50)
        else:
            print("No students found.")
    except Exception as e:
        print(f"Error retrieving students: {e}")
    finally:
        session.close()