# project Name #

`Student Registration System`
A simple command-line interface (CLI) application for managing student and course data. This system allows users to add, update, delete, and list students and courses, with all data stored in a local SQLite database.

## project features ##

`add student` to add a new student with name, email, phone and address.
`update student` to update student existing information.
`delete student` to delete student from database.
`student list` to list all student in database.
`add course` to add new course.
`update course` to update the existing course.
`delete course` to delete out the exist course in database.
`course list` to list all the courses in the database.
`Exit` to exist out from the project. 

### project usage ###

Simply type the number corresponding to your desired action and press Enter. The system will then prompt you for the necessary information.
         *** Example ***
         python3 debug.py or python debug.py

          ==== it show the below format ===

========================================
Students Registration System
========================================
1. Add Student
2. Update Student
3. Delete Student
4. List Students
5. Add Course
6. Update Course
7. Delete Course
8. List Courses
9. Exit
========================================
Enter your choice (1-9): 1 
 == then tap enter ==

        Add New Student
        Enter student name:  kuron
        == then tap enter == 

        Enter student email: kuron@gmail.com
        == then tap enter == 

        Enter student phone (optional): 0712345678
        == then tap enter == 

        Enter student address (optional): Nairobi
        == then tap enter == 

        == it done you check in the database or enter 4 to check student list ==

#### project structure ####


|- `main.py`          # Main application logic and the entry point. Contains the main loop and user interaction.
|- `database.py`      # Handles database connection and initialization.
|- `student.py`       # Contains all functions related to student CRUD (Create, Read, Update, Delete) operations.
|- `course.py`        # Contains all functions related to course CRUD operations.
|- `school.db`      # SQLite database file.
|- `debug.py`      # to Navigate to the project directory in your terminal or command prompt.

##### project installation #####

1 - `Clone the Repository`
First, clone the repository from GitHub to your local machine using git:  
`git clone git@github.com:David-kuron1996/students-and-courses-registration-project.git`

Navigate into the project directory:
`cd` your-repo-name
