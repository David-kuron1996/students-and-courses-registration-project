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
