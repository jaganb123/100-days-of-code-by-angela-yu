# generate bill based on user choice
# We have pizza in 3 sizes, Small $15, Medium $20, Large $25
# Toppings Pepperoni small +$2, Medium or Large +$3
# Add Extra cheese +$1 for all sizes
# print out the bill..

##Example Input

# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"

print("Welcome to the Jagan's Pizza World!!!")
Pizza = input("Choose size of the PIZZA ? S, M, L ? ").lower()
Topping = input("Do you need Pepperonni topping ? Y/N ").lower()
AddCheese = input("Need some extra cheese ? Y/N ").lower()

FinalPrice = 0
if "s" in Pizza:
    FinalPrice += 15
elif "m" in Pizza:
    FinalPrice += 20
elif "l" in Pizza:
    FinalPrice += 25
else:
    print("Please enter valid choice, exiting now, byeeee...")
    exit(1)
if "y" in Topping:
    if "s" in Pizza:
        FinalPrice += 2
    else:
        FinalPrice += 3
if "y" in AddCheese:
    FinalPrice += 1
print(f"Your bill is: ${FinalPrice}")
