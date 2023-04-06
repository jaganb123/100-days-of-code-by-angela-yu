# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

from random import choice

Payee = choice(names)
print(f"{Payee} gonna pay the bill, Hola...")
