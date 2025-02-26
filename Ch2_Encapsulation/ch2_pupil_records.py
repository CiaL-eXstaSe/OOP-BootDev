"""
===============================
Pupil Records
===============================

Players can recruit wizard pupils into their armies. Depending on the pupil's marks, 
they gain different in-game abilities.

===============================
Assignment
===============================
Complete the Student class.

-----------------
Constructor
-----------------
* The constructor should set the name parameter to the name instance variable
* Should initialize a private data member called __courses to an empty dictionary

-----------------
Methods
-----------------
calculate_letter_grade:
* Takes a score parameter
* Returns letter grade based on score:
    - "A" for 90 or above
    - "B" for 80-89
    - "C" for 70-79
    - "D" for 60-69
    - "F" for below 60

add_course:
* Takes course_name and score parameters
* Calculates letter grade using calculate_letter_grade
* Adds course_name (key) and letter grade (value) to courses dictionary

get_courses:
* Returns the private __courses dictionary
"""

class Student:
    # Constructor initializes a new Student object
    # name: public attribute for student identification
    # __courses: private dictionary to store course grades (name-to-grade mapping)
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    # Converts numerical scores to letter grades using standard grading scale
    # score: numerical grade (0-100)
    # returns: corresponding letter grade (A, B, C, D, or F)
    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    # Adds a new course and its grade to the student's record
    # course_name: name of the course to add
    # score: numerical score received in the course
    # The score is converted to a letter grade before storing
    def add_course(self, course_name, score):
        self.__courses[course_name] = self.calculate_letter_grade(score)
        
    # Getter method to access the private courses dictionary
    # Returns: dictionary of all courses and their letter grades
    # This maintains encapsulation while allowing read access to the data
    def get_courses(self):
        return self.__courses