from database import get_db_connection

def add_course(name, code, description=None):
    """Add a new course to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO courses (name, code, description) VALUES (?, ?, ?)",
            (name, code, description)
        )
        conn.commit()
        print(f"Course {name} ({code}) added successfully!")
        return True
    except sqlite3.IntegrityError:
        print("Error: A course with this code already exists.")
        return False
    except Exception as e:
        print(f"Error adding course: {e}")
        return False
    finally:
        conn.close()

def update_course(course_id, name=None, code=None, description=None):
    """Update course information."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Build the update query dynamically
    fields = []
    values = []
    
    if name:
        fields.append("name = ?")
        values.append(name)
    if code:
        fields.append("code = ?")
        values.append(code)
    if description:
        fields.append("description = ?")
        values.append(description)
    
    if not fields:
        print("No fields to update.")
        return False
    
    values.append(course_id)
    query = f"UPDATE courses SET {', '.join(fields)} WHERE id = ?"
    try:
        cursor.execute(query, values)
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Course with ID {course_id} updated successfully!")
            return True
        else:
            print(f"Course with ID {course_id} not found.")
            return False
    except sqlite3.IntegrityError:
        print("Error: A course with this code already exists.")
        return False
    except Exception as e:
        print(f"Error updating course: {e}")
        return False
    finally:
        conn.close()

def delete_course(course_id):
    """Delete a course from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Course with ID {course_id} deleted successfully!")
            return True
        else:
            print(f"Course with ID {course_id} not found.")
            return False
    except Exception as e:
        print(f"Error deleting course: {e}")
        return False
    finally:
        conn.close()

