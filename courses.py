#CourseFullException: Raised when PremiumCourse enrollment limit is reached
class CourseFullException(Exception):
    "Raised when a PremiumCourse reaches its enrollment limit"
    pass

# Create a base class with a method enroll(self, course, user_id) that raises NotImplementedError with a message like "Subclasses must implement enroll".
class EnrollmentStrategy:
    def enroll(self, course, user_id):
        raise NotImplementedError("Subclasses must implement enroll")

#Defines the "unlimited enrollment" behavior for free courses.
class FreeEnrollmentStrategy(EnrollmentStrategy):
    def enroll(self, course, user_id):
        pass

#Check if course.current_enrollments >= course.max_enrollments.
class PremiumEnrollmentStrategy(EnrollmentStrategy):
    def enroll(self, course, user_id):
        if course.current_enrollments >= course.max_enrollments:
            raise CourseFullException
        course.current_enrollments += 1
        if course.current_enrollments == course.max_enrollments:
            course.is_available = False




# Define course-related classes with inheritance and polymorphism
class Course():
    
    def __init__(self, title, item_id, instructor, enrollment_strategy):
        self.title = title
        self.item_id = item_id
        self.instructor = instructor
        self.enrollment_strategy = enrollment_strategy
        self.is_available = True
        self.enrolled_users = []
            
            
    # Returns a string with basic course details        
    def get_info(self):
        return f"title: {self.title}, instructor: {self.instructor}, available: {self.is_available}"
    
    
    # Handles the logic for a user enrolling in this course
    def enroll_user(self, user_id):
        self.enrollment_strategy.enroll(self, user_id)
        self.enrolled_users.append(user_id)

    def check_availability(self):
        return self.is_available




class FreeCourse(Course):
    
    def __init__(self, title, item_id, instructor):
        super().__init__(title, item_id, instructor, FreeEnrollmentStrategy())
   
    def get_info(self):
        return super().get_info + "free"
 


class PremiumCourses(Course):
    
    def __init__(self, title, item_id, instructor, is_availableprice, price, max_enrollments):
        super().__init__(title, item_id, instructor, is_availableprice, PremiumEnrollmentStrategy())
        self.price = price
        self.max_enrollments = max_enrollments
        self.current_enrollments = 0
    
    def get_info(self):
        return super().get_info + f"(Premium, Price: ${self.price}, Enrollments: {self.current_enrollments}/{self.max_enrollments})"
    


class CreateCourse:
    
    def create_course(self,course_type, course_id, title, instructor, **kwargs):
        if course_type == "free":
            return FreeCourse(course_id, title, instructor)
        elif course_type == "premium":
            price = kwargs.get("price")
            max_enrollment = kwargs.get("max_enrollment")
            if price is None or max_enrollment is None:
                raise ValueError("Premium courses require price and max_enrollments")
            return PremiumCourses(course_id, title, instructor, price, max_enrollment)
        else:
            raise ValueError("Invalid course type")




