'''
input:3
output:March

 input:5
 output:May
 '''
def printMonth(dn):
    if(dn==1):
        return "January"
    elif(dn==2):
        return "February"
    elif(dn==3):
        return "March"
    elif(dn==4):
        return "April"
    elif(dn==5):
        return "May"
    elif(dn==6):
        return "June"
    elif(dn==7):
        return "July"
    elif(dn==8):
        return "August"
    elif(dn==9):
        return "September"
    elif(dn==10):
        return "October"
    elif(dn==11):
        return "November"
    elif(dn==12):
        return "December"
    else:
        return "Invalid"
    
    
for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))
