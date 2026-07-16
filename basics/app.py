from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Sample database
students = {
    1: {"name": "Santhosh", "course": "Python"},
    2: {"name": "Rahul", "course": "FastAPI"}
}


# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }


# Get all students
@app.get("/students", status_code=status.HTTP_200_OK)
def get_students():
    return students


# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return students[student_id]


# Add a new student
@app.post("/students", status_code=status.HTTP_201_CREATED)
def add_student(student: dict):
    new_id = max(students.keys()) + 1
    students[new_id] = student
    return {
        "message": "Student added successfully",
        "student": students[new_id]
    }


# Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: dict):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    students[student_id] = student
    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }


# Delete student
@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    del students[student_id]