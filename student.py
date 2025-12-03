from database import get_db_connection

def add_student(name, email, phone=None, address=None):
    """Add a new student to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO students (name, email, phone, address) VALUES (?, ?, ?, ?)",
            (name, email, phone, address)
        )
        conn.commit()
        print(f"Student {name} added successfully!")
        return True
    except sqlite3.IntegrityError:
        print("Error: A student with this email already exists.")
        return False
    except Exception as e:
        print(f"Error adding student: {e}")
        return False
    finally:
        conn.close()
def update_student(student_id, name=None, email=None, phone=None, address=None):
    """Update student information."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Build the update query dynamically
    fields = []
    values = []
    
    if name:
        fields.append("name = ?")
        values.append(name)
    if email:
        fields.append("email = ?")
        values.append(email)
    if phone:
        fields.append("phone = ?")
        values.append(phone)
    if address:
        fields.append("address = ?")
        values.append(address)
    
    if not fields:
        print("No fields to update.")
        return False
    
    values.append(student_id)
    query = f"UPDATE students SET {', '.join(fields)} WHERE id = ?"
    
    try:
        cursor.execute(query, values)
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Student with ID {student_id} updated successfully!")
            return True
        else:
            print(f"Student with ID {student_id} not found.")
            return False
    except sqlite3.IntegrityError:
        print("Error: A student with this email already exists.")
        return False
    except Exception as e:
        print(f"Error updating student: {e}")
        return False
    finally:
        conn.close()

def delete_student(student_id):
    """Delete a student from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Student with ID {student_id} deleted successfully!")
            return True 
        else:
            print(f"Student with ID {student_id} not found.")
            return False
    except Exception as e:
        print(f"Error deleting student: {e}")
        return False
    finally:
        conn.close() 
