#dictionary as switch
def PrintSunday():
    print('Sunday')
    return
def PrintMonday():
    print('Monday')
def PrintTuesday():
    print('Tuesday')
def PrintWednesday():
    print('Wednesday')
def PrintThursday():
    print('Thursday')
def PrintFriday():
    print('Friday')
def PrintSaturday():
    print('Saturday')
def choice():
    print("Enter day number between 1-7")
    return
daySelect={1:PrintSunday, 2:PrintMonday, 3:PrintTuesday, 4:PrintWednesday,
           5:PrintThursday, 6:PrintFriday, 7:PrintSaturday}
choice()
dayNum=int(input())
if dayNum>=1 and dayNum<=7:
    daySelect[dayNum]()
else:
    print( "INVALID")

