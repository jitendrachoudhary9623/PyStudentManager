students=[]

def get_student_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase=student["name"].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase=get_student_titlecase()
    print(students_titlecase)

def add_student(name,student_id):
    student={"name":name,"student_id":student_id}
    students.append(student)

student_list=get_student_titlecase()

true=True;
while(true):
    student_name=input("Enter Student Name")
    student_id=input("Enter Student Id")
    add_student(student_name,student_id)
    add_more=input("Add More Students? (yes/no)")
    if(add_more=="no"):
        true=False



print_students_titlecase()