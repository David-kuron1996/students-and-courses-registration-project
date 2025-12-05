from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import os

# Database setup
DB_NAME = "school.db"
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String)
    address = Column(String)
    created_at = Column(DateTime, default=func.current_timestamp())
    
    # Relationship to enrollments
    enrollments = relationship("Enrollment", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False, unique=True)
    description = Column(String)
    created_at = Column(DateTime, default=func.current_timestamp())
    
    # Relationship to enrollments
    enrollments = relationship("Enrollment", back_populates="course")

class Enrollment(Base):
    __tablename__ = 'enrollments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    enrolled_at = Column(DateTime, default=func.current_timestamp())
    
    # Relationships
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

def get_db_connection():
    """Create a connection to the SQLite database using SQLAlchemy."""
    if not os.path.exists(DB_NAME):
        engine = create_engine(f'sqlite:///{DB_NAME}')
        Base.metadata.create_all(engine)
    else:
        engine = create_engine(f'sqlite:///{DB_NAME}')
    
    Session = sessionmaker(bind=engine)
    return Session()

def init_db():
    """Initialize the database and create tables if they don't exist."""
    engine = create_engine(f'sqlite:///{DB_NAME}')
    Base.metadata.create_all(engine)