# Student Class - Defines the student object
class Student: 

    grade = 0
    passing_score = 75
    award_credit = False

    #initializer sometimes called a contructor
    def __init__(self, first_name, last_name, status):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name.lower + self.last_name.lower + '@weber.edu'
        self.status = status

    def print_student_info(self):
        print('STUDENT:', self.first_name, self.last_name, 'EMAIL:', self.email, 'STATUS:', self.status)

    def set_grade(self, new_grade):
        self.grade = new_grade
        if (self.grade >= self.passing_score):
            self.award_credit = True
        if (self.grade < self.passing_score):
            self.award_credit = False

Ruik = Student('Ruik', 'Silver', 'Full time') # Ruik is an instance of the Student class
Khliomer = Student('Khliomer', 'Schmebulok', 'Part time') # Khliomer is an instance of the Student class

Ruik.set_grade(80)
print '\n'
Khliomer.set_grade(74)
print '\n'

Ruik.print_student_info
Khliomer.print_student_info

print('\n,\n', Ruik.grade)