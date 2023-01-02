#merge two python dictionaries into one
dict1={'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2={'Fourty': 40, 'Fifty': 50, 'Sixty': 60}
dict3={**dict1,**dict2}
print(dict3)
