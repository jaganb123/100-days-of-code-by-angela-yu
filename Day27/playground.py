def add(*val):
    total = 0
    for i in val:
        total += i
    return total

print(add(10, 11, 23, 34, 56, 77, 89, 123))