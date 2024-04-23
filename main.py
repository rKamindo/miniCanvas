from fastapi import Depends, FastAPI
from typing import List
from course import CourseManager, Course
from user import UserManager
from fastapi.security import APIKeyHeader

user_manager = UserManager()
course_manager = CourseManager()

user_manager.create_a_user("John", "pwd", "student")
user_manager.create_a_user("Alice", "pwd", "teacher")
user_manager.create_a_user("Jimmy", "pwd", "admin")

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to our miniCanvas!"

@app.post("/courses/{coursecode}")
def create_a_course(coursecode: str, 
                    semester: str, 
                    teacher_id_list: List[int]
    ) -> int:    
    ### an admin should create a course
    teacher_list = user_manager.find_users(teacher_id_list)
    course_id = course_manager.create_a_course(coursecode, semester, teacher_list)

    return course_id

@app.put("/courses/{courseid}/students")
def import_students(courseid: int,
                    student_id_list: List[int]) -> None:
    course = coursemanager.find_a_course(courseid)
    student_list = usermanager.find_users(student_id_list)
    course.import_students(student_list)
    
    print(course.course_id)
    print(course.student_list)
    
    return None