class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print('Name : '+self.name.title()+'\nRollno : ' +str(self.rollno))
        print('College : '+self.college+'\nCourse : ' +self.course)
for j in range(2):
    n=input()
    r=int(input()) 
    obj=Student(n,r)
    obj.displayStudent()
