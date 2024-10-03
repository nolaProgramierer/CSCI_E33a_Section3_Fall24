# Import models from student app
from student.models import *

# 1) Create a new advisor
advisor1 = Advisor(fname="Christian", lname="Tielemann")
advisor1.save()

# 2) Create a new course
course1 = Course(dept="MUS", course_num=224, subject="Music Theory2")
course1.save()

# 3) Create a new student
student1 = Student(fname="Lionel", lname="Rednick", student_advisor=advisor1)
student1.save()
student1

# 4) Assign a student to the course
course1.students.add(student1)
course1.save()
course1

# 5) Make another student
student2 = Student(fname="Emily", lname="Bryan", student_advisor=advisor1)
student2.save()
student2

# 6) Add this student to the course from the other side of the relationship
student2.courses.add(course1)
student2.save()

# 7) Find all courses a student is enrolled in
student1.courses.all()

# 8) Find all students in a particular course
course1.students.all()

# 9) Add an advisor to a student
student1.student_advisor = advisor1
student1.save()
student1.student_advisor

# 10)Show all advisees of Albert Einstein
advisor1.advisees.all()

# 11) Find all active student
active_students = Student.objects.filter(active=True)
active_students

# 12) Find students with no advisor
students_wo_advisors = Student.objects.filter(student_advisor__isnull=True)
students_wo_advisors

# 13) Find all students enrolled in at least one course
students_with_courses = Student.objects.filter(courses__isnull=False).distinct()
students_with_courses

# 14) Return all of Albert's advisees whose last names begin with "G"
advisor1.advisees.filter(lname__startswith="G")

# 15) Return all students in course 1
course1.students.all()

# 16) Return all the courses of student 1
student1.courses.all()

# 17) Add another course
course2 = Course(dept="HUM", course_num=355, subject="The Moors in Spain")
course2.save()

# 18) Add course to a student
student1.courses.add(course2)
student1.save()

# 19) Return all of a students courses
student1.courses.all()

# 20) Return the highest course number of a student
student1.highest_course_num()

# 21) Return the lowest course number of a student
student1.lowest_course_num()

# 22) Retrieve all students enrolled in a particular course and advised by a particular advisor
students_advised_and_enrolled = Student.objects.filter(student_advisor=advisor1, courses=course1)
students_advised_and_enrolled


