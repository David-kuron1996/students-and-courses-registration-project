# project Name #

`Student Registration System`
A simple command-line interface (CLI) application for managing student and course data. This system allows users to add, update, delete, and list students and courses, with all data stored in a local SQLite database.

## project features ##

1. `add student` to add a new student with name, email, phone and address.
2. `update student` to update student existing information.
3. `delete student` to delete student from database.
4. `student list` to list all student in database.
5. `add course` to add new course.
6. `update course` to update the existing course.
7. `delete course` to delete out the exist course in database.
8. `course list` to list all the courses in the database.
9. `list Enrollment` to list student enrollment(relation between student and course).
10. `Add Enrollment` to add enrollment(to coures to student by ID).
11. `Remove Enrollment` to delete student enrollment(by ID).
12. `Exit` to exist out from the project. 

### project usage ###

Simply type the number corresponding to your desired action and press Enter. The system will then prompt you for the necessary information.

*** Example ***
       file_name%  python3 debug.py or python debug.py

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
9. list Enrollment
10. Add Enrollment
11. Remove Enrollment
12. Exit
========================================

1.       Enter your choice (1-9): 1 
            == then tap enter ==

2.        Add New Student
        Enter student name:  kuron
            == then tap enter == 

 3.       Enter student email: kuron@gmail.com
            == then tap enter == 

4.        Enter student phone (optional): 0712345678
            == then tap enter == 

5.        Enter student address (optional): Nairobi
            == then tap enter == 

        == it done you check in the database or enter 4 to check student list ==

#### project structure ####


|- `main.py`          # Main application logic and the entry point. Contains the main loop and user interaction.
|- `database.py`      # Handles database connection and initialization.
|- `student.py`       # Contains all functions related to student CRUD (Create, Read, Update, Delete) operations.
|- `course.py`        # Contains all functions related to course CRUD operations.
|- `school.db`        # SQLite database file.
|- `debug.py`         # to Navigate or run the project directory in your terminal or command prompt.
|- `enrollment`       # contains all functions related to enrollment(relation between student and course)

##### project installation #####

1. `Clone the Repository`
First, clone the repository from GitHub to your local machine using git:  
`git clone git@github.com:David-kuron1996/students-and-courses-registration-project.git`

Navigate into the project directory:
`cd` your-repo-name

2. `Install Dependencies`
All necessary Python packages are listed in the  pipfile. Install them using pipenv:

`pipenv install`

To install a specific package:

== pipenv install package_name == like `pipenv install flask`

To install dev package:
`pipenv install pytest --dev`

To activate environment:
`pipenv shell`

###### Contributing ######

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`).
3. Make your changes and commit them (`git commit -m 'Add some amazing feature`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

******* project author *******

*** Name ***: `DAVID KURON WILLIAM`

*** Project Link ***: `https://github.com/David-kuron1996/students-and-courses-registration-project.git`




