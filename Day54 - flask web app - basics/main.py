
def make_bold(function):
    def wrapper_function():
        string = str(function())
        return f"<b>{string}</b>"
    return wrapper_function

@make_bold
def name():
    return "jagan"

print(name())