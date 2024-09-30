#Module 4: Lab4
#Name : Nicolas Spain
#Date: 9/30/24
#Program Function: Calculates bonuses of certain stores and employees

def main():
    #declare local variables
    monthlySales = getsales("Enter the monthly sales: ")
    salesIncrease = getIncrease("Enter the sales increase percentage: ")
    storeAmount = calcStoreBonus(monthlySales)
    empAmount = calcEmpBonus(salesIncrease)
    printBonus(storeAmount, empAmount)
def getsales(prompt):
    monthlySales = float(input(prompt))
    return monthlySales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100
    return salesIncrease
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount
def printBonus(storeAmount, empAmount):
    print("Store Bonus: $", storeAmount)
    print("Employee Bonus: $", empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print("Congratulations! You have earned the maximum bonus!")
main()

