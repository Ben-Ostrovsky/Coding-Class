
#Define Elements
annualSalary=float(input("ANNUAL SALARY: "))
portion_down_payment=0.25
currentSavings=0
r=0.04
monthlySalary=annualSalary/12.0
portionSaved=(float(input("PORTION SAVED: ")))
totalCost=float(input("TOTAL COST: "))
semiAnnualRaise=float(input("SEMI ANNUAL RAISE:"))

#Getting paid until you reach goal, each way through is considered one month
month=0
while currentSavings<(totalCost*portion_down_payment):
    month+=1
    currentSavings+=(portionSaved*monthlySalary)+(currentSavings*r/12)
    #New section for the Semi Annul Raise
    if int(month/6)==month/6:
        annualSalary+=annualSalary*semiAnnualRaise
        monthlySalary=annualSalary/12
print("Number of months", month)


    