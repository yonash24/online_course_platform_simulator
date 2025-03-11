from courses import CourseFullException
from users import AccessDeniedException

# Handles general input errors across the platform.
class InvalidInputException(Exception):
    raise 




#Implements Singleton pattern for a single platform instance.
class Platform:
    _instance = None
     
    @staticmethod
    def get_instance():
        if Platform._instance is None:
            Platform._instance = Platform()
        return Platform.instance
        
    def __init__(self):
        if Platform._instance is not None:
            raise RuntimeError("Use get_instance() to access the Platform")
        self.courses = []
        self.users = []

    def add_courses(self, course):
        if any(c.course_id == course.course_id for c in self.courses) or course.course_id < 0:
            raise InvalidInputException("Invalid or duplicate course ID")
        self.courses.append(course)
    
    def register_user(self, user):
        if any(u.use_id == user.user_id for u in self.users) or user.user_id < 0:
            raise InvalidInputException("Invalid or duplicate course ID")
        self.users.append(user)
    
    def find_course_by_id(self, course_id):
        for x in range(len(courses)):
            if courses[x].course_id == course_id:
                return courses[x]
        raise InvalidInputException(f"Course ID {course_id} not found")

    def enroll_users_in_course(self, user_id, course_id):
        for user in users:
            if user.user_id == user_id:
                return user
        raise InvalidInputException(f"User ID {user_id} not found")    
    
        course = self.find_course_by_id(course_id)
        
        try:
            user.enroll_in_course(course)
            course.enroll_user(user_id)
            return f"User {user_id} enrolled in course {course_id} successfully"
        except (CourseFullException, AccessDeniedException, ValueError) as e:
            raise InvalidInputException(str(e))  
    
    def display_all_courses(self):
        if not self.courses:
            return "No courses available"
        return "\n".join(course.get_info() for course in self.courses)