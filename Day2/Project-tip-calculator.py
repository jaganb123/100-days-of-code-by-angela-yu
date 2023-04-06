# ToDo list
# Greet the user and get the total bill amount
# get input like how much percent they would like to tip
# know how many persons to split the total bill
# print the output

print("Welcome to the Tip Calculator!..")
TotalBill = float(input("What was the total bill ? $"))
TipPercent = int(input("How much would you like to tip ? 10, 12, or 15? "))
TotalPerson = int(input("How many people to split the bill? "))

# math part

EachPay = ((TotalBill * (TipPercent + 100)) / 100) / TotalPerson

print(f"Each person should pay: ${round(EachPay, 2):.2f}")
