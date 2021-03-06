"""
Your task is to extend the implementation of the Student Manager class of Week 03
First, you should cut and paste where indicated your implementation of Week 03,
then you should complete the implementatin of the additional functions
"""

#=================== CUT & PASTE your implementation of week 02 ================================================================
#===============================================================================================================================
class Student:
    """ A simple GPA calculator
    """

    # a map linking letter grads to GPA points
    POINTS = {'A+':4.3, 'A0':4.0,'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D0':1.0}

    #constructor
    def __init__(self, student_name, student_id):
        """ create a new instance of the GPA calculator"""
        # a map of course names to letter grades for a student, e.g., self_grades["ADSA"]="A0"
        self._grades = {}
        # complete with initialisation of self._student_name and self._student_id
        pass

    def get_student_name(self):
        """ Return the name of the student """
        return self._student_name

    def get_student_id(self):
        """ Return the name of the student """
        return self._student_id


    def get_gpa(self):
        """ returns the GPA of the student """
        # this function should caluclate the GPA and print it.
        # HINT: for each course in self._grades, you need to retrieve the corresponding points from Student.POINTS (and then calculate the GPA)
        pass

    def add_grade(self, course_name, letter):
        """ Add a new grade """
        # You should improve this function by checking that the letter grade entered is correct.
        # Notice that, for instance, 'Good', 'AB', 'AB+' or 'D-' are not allowed as letter grades (only letter grades in POINTS are allowed)
        if course_name in self._grades:
            print("Cannot add -{0}-, course already registered".format(course_name))
        else:
            self._grades[course_name] = letter
            print("New grade registered")

    def print_grades(self):
        #This function should print the list of courses with the respective letter grades achieved by a student
        pass

# =============================================== END CUT AND PASTE ======================================================================
#=======================================================================================================================================================

# New methods to implement
    def update_grade(self, course_name, letter):
        """
        This method should check if a letter grade is already registered for a course
        if the a grade is already registered, then the letter grade is updated
        otherwise an error message is returned to the user, something like: "Grade not registered for course_name"
        :param course_name: the name of the course to be updated
        :param letter: the new letter grade
        """
        pass

    def get_strange_gpa(self):
        """
        this method calculates a "strange" GPA by multiplying the points value of all the grades currently registered for a student
        For example, if the following grades are registered: "ADSA":A0, "Math": B0
        then the GPA returned will be 4.0 * 3.0 = 12.0
        You should try to implement this function RECURSIVELY
        """
        pass

    def get_count_of_above_bplus(self):
        """
        This function should return the number of courses passed by a student with a grade equal to or greater than B+
        """
        pass


if __name__ == '__main__':
    # Run this test to check the correctness of your implementation

    mc = Student("Marco Comuzzi","112233")

    mc.add_grade("ADSA","A+")
    mc.add_grade("Math101", "A-")
    mc.add_grade("Italian101","B0")
    mc.add_grade("Italian101","B+")

    print("{0} GPA is: {1}".format(mc.get_student_name(), mc.get_gpa()))

    mc.print_grades()

    print("========================")
    print("WEEK 03 TESTS ==========")
    print("========================")

    mc.update_grade("Korean101","C0")
    mc.update_grade("Italian101","A+")

    print("{0}'s strange GPA is: {1}".format(mc.get_student_name(), mc.get_strange_gpa()))
    print("{0}'s number of courses with B+ or above is: {1}".format(mc.get_student_name(), mc.get_count_of_above_bplus()))