# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Password = ""
# for n in range(0, nr_letters ):
#     Password += random.choice(letters)
# for n in range(0, nr_symbols ):
#     Password += random.choice((symbols))
# for n in range(0, nr_numbers ):
#     Password += random.choice(numbers)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Password = ""
# PasswordLength = nr_letters + nr_symbols + nr_numbers
# PasswordChoice = ["letters", "symbols", "numbers"]
# for n in range(0, PasswordLength):
#     Character = random.choice(PasswordChoice)
#     if Character == "letters":
#         nr_letters -= 1
#         Password += random.choice(letters)
#         if nr_letters == 0 :
#             PasswordChoice.remove("letters")
#     elif Character == "symbols" :
#         nr_symbols -= 1
#         Password += random.choice((symbols))
#         if nr_symbols == 0:
#             PasswordChoice.remove("symbols")
#     elif Character == "numbers" :
#         nr_numbers -= 1
#         Password += random.choice((numbers))
#         if nr_numbers == 0:
#             PasswordChoice.remove("numbers")

Password_list = []
for n in range(0, nr_letters):
    Password_list.append(random.choice(letters))
for n in range(0, nr_symbols):
    Password_list.append(random.choice((symbols)))
for n in range(0, nr_numbers):
    Password_list.append(random.choice(numbers))
print(Password_list)
random.shuffle(Password_list)
print(Password_list)
Password = ""
for i in Password_list:
    Password += i

print(f"Your password is : {Password}")
