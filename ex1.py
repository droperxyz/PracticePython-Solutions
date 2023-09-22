from datetime import datetime as d

def GetData():
    userName = str(input("Input your name: "))
    userAge = int(input("Input your age: "))
    copies = int(input("How many copies of output do you want?: "))
    currentYear = d.now().year
    return userName, userAge, copies, currentYear

def Calculations(userAge, currentYear):
    calc = (100 - userAge) + currentYear
    return calc

def Output(calc, copies, userName):
    for i in range(copies): 
        print(f"{userName}, you will turn 100 in {calc}!")

userName, userAge, copies, currentYear = GetData()
calc = Calculations(userAge, currentYear)
Output(calc, copies, userName)







