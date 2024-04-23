from course import CourseManager, Course

def test_create_course_successful():
  course_manager = CourseManager()
  course_id = course_manager.create_a_course("COSC381", "FALL2024", ["Prof. Jiang"])
  
  assert course_id is not None

  assert course_id in [course.course_id for course in course_manager.course_list]

def test_create_course_without_code_unsuccessful():
  course_manager = CourseManager()
  course_id = course_manager.create_a_course("", "FALL2024", ["Prof. Jiang"])

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