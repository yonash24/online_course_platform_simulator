# Entry point with console interface
from platform import Platform, InvalidInputException
from users import create_user
from courses import create_course

def main():
    platform = Platform.get_instance()
    while True:
        print("\nOnline Course Platform Simulator")
        print("1. Add Course")
        print("2. Register User")
        print("3. Enroll in Course")
        print("4. View Courses")
        print("5. View User Courses")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        try:
            if choice == "1":
                course_type = input("Course type (free/premium): ").lower()
                course_id = int(input("Course ID: "))
                title = input("Course title: ")
                if course_type == "premium":
                    price = float(input("Price: "))
                    max_enrollments = int(input("Max enrollments: "))
                    course = create_course(course_type, course_id, title, "Temp Instructor",
                                        price=price, max_enrollments=max_enrollments)
                else:
                    course = create_course(course_type, course_id, title, "Temp Instructor")
                platform.add_course(course)
                print(f"Course {course_id} added successfully")

            elif choice == "2":
                user_type = input("User type (learner/instructor): ").lower()
                user_id = int(input("User ID: "))
                name = input("Name: ")
                if user_type == "learner":
                    membership = input("Membership (basic/premium): ").lower()
                    user = create_user(user_type, user_id, name, membership_level=membership)
                else:
                    specialization = input("Specialization: ")
                    user = create_user(user_type, user_id, name, specialization=specialization)
                platform.register_user(user)
                print(f"User {user_id} registered successfully")

            elif choice == "3":
                user_id = int(input("User ID: "))
                course_id = int(input("Course ID: "))
                result = platform.enroll_user_in_course(user_id, course_id)
                print(result)

            elif choice == "4":
                print(platform.display_all_courses())

            elif choice == "5":
                user_id = int(input("User ID: "))
                user = next((u for u in platform.users if u.user_id == user_id), None)
                if user:
                    print(user.view_courses())
                else:
                    print("User not found")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice, try again")

        except (ValueError, InvalidInputException) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()