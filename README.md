# Mini Student API

## Overview

This is a simple API built using FastAPI that allows users to manage student records. The API provides endpoints to create, retrieve, update, and delete student data.

## Features

- Retrieve all students.

- Get details of a student by ID.

- Search for a student by name.

- Create a new student.

- Update an existing student's details.

- Delete a student.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python (>=3.7)

- FastAPI

- Uvicorn

## Installation

Follow these steps to set up and run the project:

- Create a virtual environment (optional but recommended):

```sh
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

- Install the required dependencies:

```sh
pip install fastapi uvicorn
```

## Running the API

To start the FastAPI server, run:

```sh
uvicorn main:app --reload
```

Here:

- `main` refers to the Python file (`main.py`), which contains the FastAPI instance.

- `app` is the FastAPI instance.

- `--reload` enables auto-reloading when code changes (useful for development).

Once the server starts, the API can be accessed at:

- Base URL: `<http://127.0.0.1:8000>`

- Interactive API docs: `<http://127.0.0.1:8000/docs>`

- Alternative API docs: `<http://127.0.0.1:8000/redoc>`

## API Endpoints

### 1. Retrieve all students

- Endpoint: `GET /students`

- Description: Returns a list of all students.

- Response:

  ```json
  {
    "1": { "name": "John", "age": 17, "year": "Senior" },
    "2": { "name": "Jane", "age": 16, "year": "Junior" }
  }
  ```

### 2. Get a student by ID

- Endpoint: `GET /students/{student_id}`

- Description: Returns details of a student by their ID.

- Parameters:

  - `student_id` (integer) – ID of the student.

- Response:

```json
{ "name": "John", "age": 17, "year": "Senior" }
```

### 3. Search for a student by name

- Endpoint: `GET /get-by-name`

- Description: Searches for a student by name.

- Query Parameters:

  - `name` (string) – The name of the student to search for.

- Response:

```json
{ "name": "Jane", "age": 16, "year": "Junior" }
```

### 4. Create a new student

- Endpoint: `POST /create-student/{student_id}`

- Description: Creates a new student.

- Parameters:

  - `student_id` (integer) – Unique ID for the student.

- Request Body:

```json
{
  "name": "Mike",
  "age": 18,
  "year": "Senior"
}
```

- Response:

```json
{ "name": "Mike", "age": 18, "year": "Senior" }
```

### 5. Update an existing student

- Endpoint: `PUT /update-student/{student_id}`

- Description: Updates student details.

- Parameters:

  - `student_id` (integer) – ID of the student to update.

- Request Body:

```json
{
  "name": "Mike Updated",
  "age": 19,
  "year": "Graduated"
}
```

- Response:

```json
{ "name": "Mike Updated", "age": 19, "year": "Graduated" }
```

### 6. Delete a student

- Endpoint: `DELETE /delete-student/{student_id}`

- Description: Deletes a student record.

- Parameters:

  - `student_id` (integer) – ID of the student to delete.

- Response:

```json
{ "message": "Student deleted successfully" }
```

## Project Structure

```sh
student_api/
│── main.py  # Main FastAPI application file
│── requirements.txt  # Dependencies
│── README.md  # Project documentation
```

## Error Handling

The API provides meaningful error responses for cases like:

- Student not found

- Student already exists

- Invalid input data

## Testing the API

You can test the API using:

- Swagger UI: Navigate to `<http://127.0.0.1:8000/docs>`

- cURL: Example request to fetch all students:

  ```sh
  curl -X 'GET' '<http://127.0.0.1:8000/students>' -H 'accept: application/json'
  ```

- Postman: Import the endpoints and test with custom requests.

## Future Enhancements

- Connect to a database instead of using an in-memory dictionary.

- Implement authentication and authorization.

- Add more filtering and sorting options.

## Author

Ayomide Kayode

## License

MIT License
