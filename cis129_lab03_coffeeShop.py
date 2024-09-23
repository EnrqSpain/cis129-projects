print("***************************************")
print("My Coffee Shop")
Coffee = input("How many cups of coffee? ")
CoffeeCost = int(Coffee) * 5
Muffin = input("How many muffins? ")
Cookie = input("How many cookies? ")
CookieCost = int(Cookie) * 2
Tea = input("How many teas? ")
TeaCost = int(Tea) * 3
print("***************************************")
MuffinCost = int(Muffin) * 4
Tax = (CoffeeCost + MuffinCost + CookieCost + TeaCost) * .06
Total = CoffeeCost + MuffinCost + Tax + CookieCost + TeaCost
print("My Coffee Shop Receipt")
print("Coffee:" + Coffee + " @ $5.00 = $", CoffeeCost)
print("Muffin:" + Muffin + " @ $4.00 = $", MuffinCost)
print("Cookie:" + Cookie + " @ $2.00 = $", CookieCost)
print("Tea:" + Tea + " @ $3.00 = $", TeaCost)
print("6% Tax: $", Tax)
print("-----------")
print("Total: $", Total)
print("***************************************")
print("Thank you for shopping with us! We hope you come again!")
