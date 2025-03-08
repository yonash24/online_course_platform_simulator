class Course():
    
    def __init__(self, title, item_id, is_available):
        pass
    
    def get_info(self):
        pass
    
    def enroll_user(self):
        pass

    def check_availability(self):
        pass




class FreeCourse(Course):
    
    def __init__(self, title, item_id, is_available):
        pass
    
    def get_info(self):
        pass
    
    def enroll_user(self):
        pass




class PremiumCourses(Course):
    
    def __init__(self, title, item_id, is_availableprice, max_enrollments):
        pass
    
    def get_info(self):
        pass
    
    def enroll_user(self):
        pass







#CourseFullException: Raised when PremiumCourse enrollment limit is reached
class CourseFullException:
    pass



