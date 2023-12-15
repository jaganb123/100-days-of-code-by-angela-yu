def infiniteGenerator(num: int=1):
    while True:
        yield num
        num += 1

def palindrome_check(num: int):
    if num // 10 == 0:
        return False
    
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    if num == reversed_num:
        return num
    else:
        return False

gen = infiniteGenerator()
for _ in range(100000):
    check_palindrome = palindrome_check(next(gen))
    if check_palindrome:
        print(check_palindrome)
