Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
dict1={'Name':'Zara','Age':7,'Class':'First'}
print(dict1)
{'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict1['Name'])
Zara
print(dict1['Class'])
First
dict1['Age']=8
print(dic1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(dic1)
NameError: name 'dic1' is not defined. Did you mean: 'dict1'?
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Class': 'First'}
dict1['Course']='MCA'
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Class': 'First', 'Course': 'MCA'}
del dict1['Class']
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Course': 'MCA'}
del dict1
print(dict1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(dict1)
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
dict1.keys()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dict1.keys()
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
dict1={'Name':'Zara','Age':7,'Class':'First'}
dict1.keys()
dict_keys(['Name', 'Age', 'Class'])
dict1.values()
dict_values(['Zara', 7, 'First'])
dict1.items()
dict_items([('Name', 'Zara'), ('Age', 7), ('Class', 'First')])
for i in dict1:print(i)

Name
Age
Class
for i in dict1.keys():print(i)

Name
Age
Class
for i,j in dict1.items():print(i,j)

Name Zara
Age 7
Class First
