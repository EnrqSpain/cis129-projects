print("***************************************")
print("My Coffee Shop")
Coffee = input("How many cups of coffee? ")
CoffeeCost = int(Coffee) * 5
Muffin = input("How many muffins? ")
print("***************************************")
MuffinCost = int(Muffin) * 4
Tax = (CoffeeCost + MuffinCost) * .06
Total = CoffeeCost + MuffinCost+ Tax
print("My Coffee Shop Receipt")
print("Coffee:" + Coffee + " @ $5.00 = $", CoffeeCost)
print("Muffin:" + Muffin + " @ $4.00 = $", MuffinCost)
print("6% Tax: $", Tax)
print("-----------")
print("Total: $", Total)
print("***************************************")

