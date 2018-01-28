students=[]
class Student:
    #self is similar to this
    school_name="R&DE School"
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


#Inheritance

class CollegeStudent(Student):
    school_name = "MESCOE,Wadia"

    #Overiding the parents memeber function
    def get_school_name(self):
        return "This is College Student"


    #super keyword
    def get_capital(self):
        parent=super().get_capital()
        return parent+" -CS"

s=CollegeStudent("Jitendra")
print(s.get_capital())