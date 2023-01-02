#initialize dictionary with default values
employees=['John','Emma']
defaults={"designation":'Developer',"Salary":80000}
data=dict.fromkeys(employees,defaults)
for i in employees:
    data[i]=defaults
print(data)

#individual data
print(data["Emma"])
