class Employee:
     empCount=0
     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
         Employee.empCount+=1
     def displayCount(self):
         print("Total Employee {0} ".format(Employee.empCount))
     def displayEmployee(self):
         print("Name :",self.name,",Salary:",self.salary)
emp1=Employee("Nikhil",9999)
emp1.displayEmployee()
emp1.displayEmployee()
emp1.salary=17000 #modify 'salary' attribute
emp1.experience=3 #add an experience attribute
emp1.displayEmployee()
emp1.name='Mahi'#modify name attribute
emp1.displayCount()
print(emp1.experience)
#del emp1.salary #dalete salary attribute
emp1.displayEmployee()
