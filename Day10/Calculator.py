def add(n1, n2):
    return n1 + n2


def subract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subract,
    "*": multiply,
    "/": divide
}
Done = False
num1 = float(input("Enter first number : "))
while not Done:
    num2 = float(input("Enter next number : "))
    for i in operations:
        print(i)
    operation_symbol = input("pick the operation : ")
    operation_function = operations[operation_symbol]
    answer = operation_function(n1=num1, n2=num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Do you want to continue calculatio with {answer}, 'y' to continue, 'n' to exit... ? ") == "y":
        num1 = answer
    else:
        print("Bye Bye !!!")
        Done = True
