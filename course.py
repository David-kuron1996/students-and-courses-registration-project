from database import get_db_connection, Course

def add_course(name, code, description=None):
    """Add a new course to the database."""
    session = get_db_connection()
    
    try:
        # Check if course with this code already exists
        existing_course = session.query(Course).filter_by(code=code).first()
        if existing_course:
            print("Error: A course with this code already exists.")
            return False
            
        new_course = Course(name=name, code=code, description=description)
        session.add(new_course)
        session.commit()
        print(f"Course {name} ({code}) added successfully!")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error adding course: {e}")
        return False
    finally:
        session.close()

def update_course(course_id, name=None, code=None, description=None):
    """Update course information."""
    session = get_db_connection()
    
    try:
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            print(f"Course with ID {course_id} not found.")
            return False
            
        # Check if code is being updated and if it's already used by another course
        if code and code != course.code:
            existing_course = session.query(Course).filter_by(code=code).first()
            if existing_course:
                print("Error: A course with this code already exists.")
                return False
        
        # Update fields if provided
        if name:
            course.name = name
        if code:
            course.code = code
        if description:
            course.description = description
            
        session.commit()
        print(f"Course with ID {course_id} updated successfully!")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error updating course: {e}")
        return False
    finally:
        session.close()

def delete_course(course_id):
    """Delete a course from the database."""
    session = get_db_connection()
    
    try:
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            print(f"Course with ID {course_id} not found.")
            return False
            
        session.delete(course)
        session.commit()
        print(f"Course with ID {course_id} deleted successfully!")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error deleting course: {e}")
        return False
    finally:
        session.close()

def list_courses():
    """List all courses in the database."""
    session = get_db_connection()
    
    try:
        courses = session.query(Course).all()
        
        if courses:
            print("\nCourses List:")
            print("=" * 50)
            for course in courses:
                print(f"ID: {course.id}")
                print(f"Name: {course.name}")
                print(f"Code: {course.code}")
                print(f"Description: {course.description or 'N/A'}")
                print(f"Created At: {course.created_at}")
                print("-" * 50)
        else:
            print("No courses found.")
    except Exception as e:
        print(f"Error retrieving courses: {e}")
    finally:
        session.close()