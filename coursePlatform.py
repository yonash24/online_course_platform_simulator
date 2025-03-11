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

    def add_courses(self):
        pass
    
    def register_user(self):
        pass
    
    def find_course_by_id(self):
        pass

    def enroll_users_in_course(self):
        pass
    
    def display_all_courses(self):
        pass