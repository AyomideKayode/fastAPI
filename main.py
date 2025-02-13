# /usr/bin/python3

""" This is a simple API that returns a list of students
    and their details.
    The API has the following routes:
    1. /students - returns a list of all students
    2. /students/{student_id} - returns the details of a student
"""

from fastapi import FastAPI, Path, HTTPException, Query
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

# create an instance of the FastAPI class
app = FastAPI()

# mock student data
students: List[Dict] = [
    {"id": 1, "name": "John", "age": 17, "year": "Senior"},
    {"id": 2, "name": "Jane", "age": 16, "year": "Junior"},
    {"id": 3, "name": "Sarah", "age": 15, "year": "Sophomore"},
    {"id": 4, "name": "David", "age": 14, "year": "Freshman"},
    {"id": 5, "name": "Michael", "age": 18, "year": "Senior"},
    {"id": 6, "name": "Emily", "age": 17, "year": "Junior"},
    {"id": 7, "name": "Grace", "age": 16, "year": "Sophomore"},
    {"id": 8, "name": "James", "age": 15, "year": "Freshman"},
    {"id": 9, "name": "Joseph", "age": 14, "year": "Freshman"},
    {"id": 10, "name": "Daniel", "age": 18, "year": "Senior"}
]

# create a Pydantic model for the student data


class Student(BaseModel):
    name: str
    age: int
    year: str


# create a Pydantic model for updating student data


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# define the get route


@app.get("/")
def index():
    return {"message": "Mini student API"}

# define the get route for /students


@app.get("/students")
def all_students():
    if not students:
        return {"message": "No students found"}
    return students


# define the get route to get student by id - path parameter
@app.get("/students/{student_id}")
def get_student(student_id: int = Path(...,
                                       description="ID of student you want to view", gt=0)):
    student = next(
        (student for student in students if student["id"] == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student


# define route to get student by name - query parameter
@app.get("/students/by-name")
def get_student(name: str = Query(..., description="Name of student to get")):
    # get student by name (case sensitive)
    student = next(
        (s for s in students if s["name"].lower() == name.lower()), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student


# combine path and query parameters
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None):
    student = next(
        (student for student in students if student["id"] == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student


# define route to create a new student
@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    # Check if student_id already exists
    if any(s["id"] == student_id for s in students):
        raise HTTPException(status_code=400, detail="Student already exists")
    # create new student dictionary
    new_student = {"id": student_id, **student.dict()}
    # append new student to students list
    students.append(new_student)

    return {"message": "Student added successfully", "student": new_student}


# define route to update student details
@app.put("/students/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    # Find student by ID
    student_record = next((s for s in students if s["id"] == student_id), None)

    if student_record is None:
        raise HTTPException(status_code=404, detail="Student does not exist")

    # Update only fields that are provided
    if student.name is not None:
        student_record["name"] = student.name
    if student.age is not None:
        student_record["age"] = student.age
    if student.year is not None:
        student_record["year"] = student.year

    return {"message": "Student updated successfully", "student": student_record}


# define route to delete a student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    global students  # Modify the global students list

    # Find student by ID
    student_record = next((s for s in students if s["id"] == student_id), None)

    if student_record is None:
        raise HTTPException(status_code=404, detail="Student does not exist")

    # Remove student from the list
    students = [s for s in students if s["id"] != student_id]

    return {"message": "Student deleted successfully"}
