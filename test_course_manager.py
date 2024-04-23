from unittest import mock

from assignment import Assignment, Submission
from course import Course, CourseManager
from unittest.mock import patch
from main import create_a_course, import_students,  course_manager
from user import User


@patch('user.UserManager.find_users')
def test_create_course_successful(mock_find_users):
  mock_teacher1 = mock.Mock(spec=User, type="teacher")
  mock_teacher2 = mock.Mock(spec=User, type="teacher")
  mock_find_users.return_value = [mock_teacher1, mock_teacher2]

  course_id = create_a_course("COSC381", "FALL2024", [1, 2])
  
  assert course_id is not None
  mock_find_users.assert_called_once_with([1, 2])
  assert course_id in [course.course_id for course in course_manager.course_list]



@patch('user.UserManager.find_users')
def test_create_course_without_code_unsuccessful(mock_find_users):
  mock_teacher1 = mock.Mock(spec=User, type="teacher")
  mock_teacher2 = mock.Mock(spec=User, type="teacher")
  mock_find_users.return_value = [mock_teacher1, mock_teacher2]

  course_id = create_a_course("", "FALL2024", [1, 2])
  
  assert course_id is None
  assert course_id not in [course.course_id for course in course_manager.course_list]

def test_find_a_course_exists_successful():
  course_manager = CourseManager()
  expectedCourse = Course(1, "COSC381", "FALL2024", ["Prof. Jiang"])
  course_manager.course_list.append(expectedCourse)

  actualCourse = course_manager.find_a_course(1)

  assert actualCourse is not None
  assert actualCourse.course_id == expectedCourse.course_id
  assert actualCourse.course_code == expectedCourse.course_code
  
def test_find_course_not_existing_return_none():
  course_manager = CourseManager()

  actualCourse = course_manager.find_a_course(1)

  assert actualCourse is None

@patch('user.UserManager.find_users')
@patch('course.CourseManager.find_a_course')
def test_import_students_successful(mock_find_a_course, mock_find_users):
  course = mock.Mock(spec=Course, course_id=1, course_code="COSC381", 
                          semester="FALL2024", teacher_list=["Prof. Jiang"],
                          student_list=[])
  user1 = mock.Mock(spec=User, name="Randy", password="pwd", type="student")
  user2 = mock.Mock(spec=User, name="James", password="pwd", type="student")
  mock_find_a_course.return_value = course
  mock_find_users.return_value = [user1, user2]
  
  import_students(1, [1, 2])

  mock_find_a_course.assert_called_once_with(1)
  mock_find_users.assert_called_once_with([1, 2])

def test_create_assignment_successful():
  course = Course(1, "COSC381", "FALL2024", ["Prof. Jiang"])

  assignment_id = course.create_an_assignment("04/25/2024")

  assert assignment_id is not None
  assert assignment_id in [assignment.assignment_id for assignment in  course.assignment_list]

def test_submit_assignment_successful():
  assignment = Assignment(1, "04/25/2024", 1)
  submission = Submission(1, "Sample content")

  assignment.submit(submission)

  assert submission in assignment.submission_list
