def get_user_input(prompt, input_type=str):
    """Get user input with type validation."""
    while True:
        try:
            user_input = input(prompt)
            if input_type == int:
                return int(user_input)
            elif input_type == float:
                return float(user_input)
            else:
                return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def display_menu():
    """Display the main menu options."""
    print("\nStudents Registration System")
    print("=" * 30)
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("7. List Students")
    print("4. Add Course")
    print("5. Update Course")
    print("6. Delete Course")
    print("8. List Courses")
    print("9. Exit")
    print("=" * 30)