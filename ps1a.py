#Define Elements
annualSalary=float(input("ANNUAL SALARY: "))
portion_down_payment=0.25
currentSavings=0
r=0.04
monthlySalary=annualSalary/12.0
portionSaved=(float(input("PORTION SAVED: ")))*monthlySalary
totalCost=float(input("TOTAL COST: "))

#Getting paid until you reach goal, each way through is considered one month
month=0
while currentSavings<(totalCost*portion_down_payment):
    month+=1
    currentSavings+=portionSaved+(currentSavings*r/12)
print("Number of months", month)



    