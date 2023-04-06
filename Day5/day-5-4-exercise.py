# FizzBuzz game, inn this game childrens sit in circle, and count numbers starting from 1
# like Child 1 : 1, Child 2 : 2, and if a nnumber is divisible by 3 the the children say Fizz
# Child 3 : Fizz, and if a number is divisible by 5 then children say Buzz and if a number is divisible by both 3 and 5 children say FizzBuzz


for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)
