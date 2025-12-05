# enrollment.py
from database import get_db_connection, Enrollment, Student, Course

def add_enrollment(student_id, course_id):
    """Add an enrollment relationship between a student and a course."""
    session = get_db_connection()
    
    try:
        # Check if student exists
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            print(f"Error: Student with ID {student_id} not found.")
            return False
            
        # Check if course exists
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            print(f"Error: Course with ID {course_id} not found.")
            return False
            
        # Check if enrollment already exists
        existing_enrollment = session.query(Enrollment).filter_by(
            student_id=student_id, course_id=course_id).first()
        if existing_enrollment:
            print("Error: This student is already enrolled in this course.")
            return False
            
        new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
        session.add(new_enrollment)
        session.commit()
        print(f"Student {student_id} enrolled in course {course_id} successfully!")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error adding enrollment: {e}")
        return False
    finally:
        session.close()

def remove_enrollment(enrollment_id):
    """Remove an enrollment relationship by its ID."""
    session = get_db_connection()
    
    try:
        enrollment = session.query(Enrollment).filter_by(id=enrollment_id).first()
        if not enrollment:
            print(f"Error: No enrollment found with ID {enrollment_id}.")
            return False
            
        student_id = enrollment.student_id
        course_id = enrollment.course_id
        
        session.delete(enrollment)
        session.commit()
        print(f"Student {student_id} removed from course {course_id} successfully!")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error removing enrollment: {e}")
        return False
    finally:
        session.close()

def list_enrollments():
    """List all enrollments in the database."""
    session = get_db_connection()
    
    try:
        enrollments = session.query(Enrollment).all()
        
        if enrollments:
            print("\nEnrollments List:")
            print("=" * 70)
            for enrollment in enrollments:
                student = session.query(Student).filter_by(id=enrollment.student_id).first()
                course = session.query(Course).filter_by(id=enrollment.course_id).first()
                print(f"Enrollment ID: {enrollment.id}")
                print(f"Student: {student.name} (ID: {student.id})")
                print(f"Course: {course.name} (ID: {course.id})")
                print(f"Enrolled At: {enrollment.enrolled_at}")
                print("-" * 70)
        else:
            print("No enrollments found.")
    except Exception as e:
        print(f"Error retrieving enrollments: {e}")
    finally:
        session.close()

def get_student_courses(student_id):
    """Get all courses a student is enrolled in."""
    session = get_db_connection()
    
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            print(f"Student with ID {student_id} not found.")
            return []
            
        enrollments = session.query(Enrollment).filter_by(student_id=student_id).all()
        courses = []
        
        for enrollment in enrollments:
            course = session.query(Course).filter_by(id=enrollment.course_id).first()
            courses.append(course)
            
        return courses
    except Exception as e:
        print(f"Error retrieving student courses: {e}")
        return []
    finally:
        session.close()

def get_course_students(course_id):
    """Get all students enrolled in a course."""
    session = get_db_connection()
    
    try:
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            print(f"Course with ID {course_id} not found.")
            return []
            
        enrollments = session.query(Enrollment).filter_by(course_id=course_id).all()
        students = []
        
        for enrollment in enrollments:
            student = session.query(Student).filter_by(id=enrollment.student_id).first()
            students.append(student)
            
        return students
    except Exception as e:
        print(f"Error retrieving course students: {e}")
        return []
    finally:
        session.close()