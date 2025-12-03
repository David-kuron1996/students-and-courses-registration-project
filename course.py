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