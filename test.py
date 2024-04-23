from course import CourseManager

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
