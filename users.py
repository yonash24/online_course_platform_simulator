class User:
    
    def __init__(self, user_id, name, enrolled_courses):
        pass
    
    def enroll_in_course(self):
        pass

    def view_courses(self):
        pass
    
    def track_progress(self):
        pass
    

class Learner(User):
    
    def __init__(self, user_id, name, enrolled_courses,membership_level):
        super().__init__(user_id, name, enrolled_courses)

    def enroll_in_course(self):
        return super().enroll_in_course()
    


class Instructor(User):
    
    def __init__(self, user_id, name, enrolled_courses,specialization):
        super().__init__(user_id, name, enrolled_courses)

    def create_course(self):
        pass
    
    def enroll_in_course(self):
        return super().enroll_in_course()



#Raised when a Learner with "basic" membership tries to enroll in a PremiumCourse.
class AccessDeniedException:
    pass

