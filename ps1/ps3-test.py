#Defining Elements
semiAnnualRaise=.07
r=.04
downpayment=.25
totalCost=1000000
totalMonths=36
salary=float(input("ANNUAL SALARY: "))

#Function for operation given a portion saved, returns the ammount of months it took to get to set goal
def job(portionSaved, annualSalary):
    month=0
    currentSavings=0
    monthlySalary=annualSalary/12
    while currentSavings<totalCost-100:
        month+=1
        currentSavings+=(portionSaved*monthlySalary)+(currentSavings*r/12)
        if int(month/6)==month/6:
            annualSalary+=annualSalary*semiAnnualRaise
            monthlySalary=annualSalary/12
    print(month)
    return month

#Bisection search to find best savings rate
month=0
steps=0
upper=1.0
lower=0.0
while month!=36:
    steps+=1
    savingsTest=(upper+lower)/2
    month=job(savingsTest, salary)
    if month>36:
        upper=savingsTest
        print(upper)
    elif month<36:
        lower=savingsTest
print("Best savings rate: ", savingsTest)
print("Steps in bisection search: ", steps)
