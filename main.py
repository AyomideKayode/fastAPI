# /usr/bin/python3

""" This is a simple API that returns a list of students
    and their details.
    The API has the following routes:
    1. /students - returns a list of all students
    2. /students/{student_id} - returns the details of a student
"""

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# create an instance of the FastAPI class
app = FastAPI()

# mock student data
students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "Senior"
    },
    2: {
        "name": "Jane",
        "age": 16,
        "year": "Junior"
    },
    3: {
        "name": "Sarah",
        "age": 15,
        "year": "Sophomore"
    }
}

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
    if len(students) == 0:
        return {"message": "No students found"}
    return students


# define the get route to get student by id - path parameter
@app.get("/students/{student_id}")
def get_student(student_id: int = Path(...,
                                       description="The ID of the student you want to view", gt=0, lt=10)):
    return students.get(student_id, {"message": "Student not found"})


# define route to get student by name - query parameter
@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"message": "Student not found"}


# combine path and query parameters
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"message": "Student not found"}


# define route to create a new student
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student
    return students[student_id]


# define route to update student details
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student does not exist"}
    if student.name is not None:
        students[student_id].name == student.name
    if student.age is not None:
        students[student_id].age == student.age
    if student.year is not None:
        students[student_id].year == student.year
    return students[student_id]



# define route to delete a student

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student does not exist"}
    del students[student_id]
    return {"message": "Student deleted successfully"}