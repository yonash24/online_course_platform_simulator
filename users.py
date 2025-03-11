from courses import create_course, PremiumCourse

#Raised when a Learner with "basic" membership tries to enroll in a PremiumCourse.
class AccessDeniedException(Exception):
    pass

#Sets up the Strategy pattern for user enrollment behaviors.
class UserEnrollmentStrategy:
    def enroll(self, user, course):
        raise NotImplementedError("Subclasses must implement enroll")



""" 
Check if course is a PremiumCourse (use type checking).

If true and user.membership_level isn’t "premium", raise AccessDeniedException.

If false, do nothing
"""
class LearnerEnrollmentStrategy(UserEnrollmentStrategy):
    def enroll(self, user, course):
        if isinstance(course, PremiumCourse) and (user.membership_level != "primium"):
            raise AccessDeniedException("Basic learners cannot enroll in premium courses")            

class InstructorEnrollmentStrategy(UserEnrollmentStrategy):
    def enroll(self, user, course):
       raise ValueError("Basic learners cannot enroll in premium courses")



class User:
    
    def __init__(self, user_id, name, enrollment_strategy):
        self.user_id = user_id
        self.name = name
        self.enrollment_strategy = enrollment_strategy
        self.enrolled_course = []
    
    def enroll_in_course(self):
        self.enrollment_strategy.enroll(self,course)
        self.enroll_in_course.append(course.course_id)

    def view_courses(self):
        if not self.enrolled_course:
            return "no courses enrolled"
        return "Enrolled in: " + ", ".join(str(cid) for cid in self.enrolled_courses)
    
    
    def track_progress(self):
        return "Progress tracking not implemented yet" 
    

class Learner(User):
    
    def __init__(self, user_id, name, membership_level):
        super().__init__(user_id, name, LearnerEnrollmentStrategy())
        self.membership_level = membership_level

    def enroll_in_course(self):
        return super().enroll_in_course()
    


class Instructor(User):
    
    def __init__(self, user_id, name, enrolled_courses,specialization):
        super().__init__(user_id, name, enrolled_courses, InstructorEnrollmentStrategy())
        self.specialization = specialization
        

    def create_course(self, course_type, course_id, title, **kwargs):
        return create_course(course_type, course_id, title, **kwargs)
    
    def create_user(self,user_type, user_id, name, **kwargs):
        if user_type == "Learner":
            membership_level = kwargs.get("membership level", "basic")
            return Learner( user_id, name, membership_level)
        elif user_type == "instructor":
            specialization = kwargs.get("specialization")
            if specialization is None:
                raise ValueError("Instructors require a specialization")
            return Instructor(user_id, name, specialization)
        else:
            raise ValueError("Invalid user type")



