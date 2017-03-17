#problem2
#main 함수작성
#클래스는 건들이지말고 main만 바꾸세요. ouput을 얻도록
class Student:
    POINTS = {'A+':4.3, 'A0':4.0,'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D0':1.0}

    def __init__(self, student_name, student_id):
        """ create a new instance of the GPA calculator"""
        # a map of course names to letter grades for a student, e.g., self_grades["ADSA"]="A0"
        self._name = student_name
        self._id = student_id
        self._grades = {}
        # complete with initialisation of self._student_name and self._student_id
        pass

    def get_student_name(self):
        """ Return the name of the student """
        return self._name

    def get_student_id(self):
        """ Return the name of the student """
        return self._id

    def get_gpa(self):
        total = 0
        for i in self._grades.keys():
            total += Student.POINTS[self._grades[i]]
        return total / len(self._grades)

    def add_grade(self, course_name, letter):
        """ Add a new grade """
        # You should improve this function by checking that the letter grade entered is correct.
        # Notice that, for instance, 'Good', 'AB', 'AB+' or 'D-' are not allowed as letter grades (only letter grades in POINTS are allowed)
        if course_name in self._grades:
            print("Cannot add -{0}-, course already registered".format(course_name))
        else:
            self._grades[course_name] = letter
            print("New grade registered")

        if(letter in Student.POINTS.keys()):
            self._grades[course_name]=letter
        else:
            print("The cource {0}'s letter is wrong : {1} ".format(course_name,letter))

    def print_grades(self):
        print("{0}'s grade is {1}".format(self._name, self._grades))
        pass

# New methods to implement
    def update_grade(self, course_name, letter):
        if (course_name in self._grades):
            self._grades[course_name] = letter
        else:
            print ("Grade not registered for course_name")

    def get_count_of_above_bplus(self):
        k=0
        for i in self._grades:
            if (Student.POINTS[self._grades[i]]>=3.3):
                k = k+1
        return k


if __name__ == '__main__':
    # Run this test to check the correctness of your implementation
    mc = Student("Marco Comuzzi", "112233")

    mc.add_grade("ADSA", "A+")
    mc.add_grade("Math101", "A-")
    mc.add_grade("Italian101", "B0")
    mc.add_grade("Italian101", "B+")

    print("{0} GPA is: {1}".format(mc.get_student_name(), mc.get_gpa()))

    mc.print_grades()

    print("========================")
    print("WEEK 03 TESTS ==========")
    print("========================")

    mc.update_grade("Korean101", "C0")
    mc.update_grade("Italian101", "A+")

    print("{0}'s number of courses with B+ or above is: {1}".format(mc.get_student_name(), mc.get_count_of_above_bplus()))