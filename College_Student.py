from Student import student

class CollegeStudent(student):
    school_name = "MESCOE,Wadia"

    #Overiding the parents memeber function
    def get_school_name(self):
        return "This is College Student"


    #super keyword
    def get_capital(self):
        parent=super().get_name_capitalize()
        return parent+" -CS"
