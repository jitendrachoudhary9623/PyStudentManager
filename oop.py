students=[]
class Student:
    #self is similar to this
    school_name="MESCOE,pune"
    def __init__(self,name, student_id=332):
        self.name=name
        self.student_id=student_id
        students.append(self)

    def __str__(self):
        return "Student "+self.name

    def get_capital(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


student=Student("Jitendra")

print(Student.school_name)
