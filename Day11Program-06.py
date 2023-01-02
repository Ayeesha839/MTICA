#merge two python dictionaries into one
#and also copy and update
dict1={'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2={'Fourty': 40, 'Fifty': 50, 'Sixty': 60}
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)

