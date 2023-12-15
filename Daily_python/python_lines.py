# friends = ['john', 'pat', 'gary', 'michael']
# for i, name in enumerate(friends):
#     print ("iteration {iteration} is {name}".format(iteration=i, name=name))

# parents, babies = (1, 1)
# while babies < 100:
#     print ('This generation has {0} babies'.format(babies))
#     parents, babies = (babies, parents + babies)

# prices = {'apple': 40, 'banana': 8}
# my_purchases = {
#     'apple': 3,
#     'banana': 12
# }

# grocery_bill = [prices[fruit] * my_purchases[fruit] for fruit in prices.keys()]
# print(f'I owe grocery store, INR {sum(grocery_bill)}')

# import sys

# try:
#     total = sum(int(arg) for arg in sys.argv[1:])
#     print("Sum = ", total)
# except ValueError:
#     print('Please pass some integers as argumennts')

# # indent your Python code to put into an email
# import glob
# # glob supports Unix style pathname extensions
# python_files = glob.glob('*.py')
# for file_name in sorted(python_files):
#     print ('    ------' + file_name)

#     with open(file_name) as f:
#         for line in f:
#             print ('    ' + line.rstrip())

#     print()

# from itertools import groupby
# lines = '''
# This is the
# first paragraph.

# This is the second.
# '''.splitlines()
# # Use itertools.groupby and bool to return groups of
# # consecutive lines that either have content or don't.
# for has_chars, frags in groupby(lines, bool):
#     if has_chars:
#         print (' '.join(frags))
# # PRINTS:
# # This is the first paragraph.
# # This is the second.

# import csv

# # need to define cmp function in Python 3
# def cmp(a, b):
#     return (a > b) - (a < b)

# # write stocks data as comma-separated values
# with open('stocks.csv', 'w', newline='') as stocksFileW:
#     writer = csv.writer(stocksFileW)
#     writer.writerows([
#         ['GOOG', 'Google, Inc.', 505.24, 0.47, 0.09],
#         ['YHOO', 'Yahoo! Inc.', 27.38, 0.33, 1.22],
#         ['CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.4901]
#     ])

# # read stocks data, print status messages
# with open('stocks.csv', 'r') as stocksFile:
#     stocks = csv.reader(stocksFile)

#     status_labels = {-1: 'down', 0: 'unchanged', 1: 'up'}
#     for ticker, name, price, change, pct in stocks:
#         status = status_labels[cmp(float(change), 0.0)]
#         print ('%s is %s (%.2f)' % (name, status, float(pct)))

# BOARD_SIZE = 12

# def under_attack(col, queens):
#     left = right = col

#     for r, c in reversed(queens):
#         left, right = left - 1, right + 1

#         if c in (left, col, right):
#             return True
#     return False

# def solve(n):
#     if n == 0:
#         return [[]]

#     smaller_solutions = solve(n - 1)

#     return [solution+[(n,i+1)]
#         for i in range(BOARD_SIZE)
#             for solution in smaller_solutions
#                 if not under_attack(i+1, solution)]
# for answer in solve(BOARD_SIZE):
#     print (answer)

# import itertools

# def iter_primes():
#      # an iterator of all numbers between 2 and +infinity
#      numbers = itertools.count(2)

#      # generate primes forever
#      while True:
#          # get the first number from the iterator (always a prime)
#          prime = next(numbers)
#          yield prime

#          # this code iteratively builds up a chain of
#          # filters...slightly tricky, but ponder it a bit
#          numbers = filter(prime.__rmod__, numbers)

# for p in iter_primes():
#     if p > 1000:
#         break
#     print (p)


def is_a_dyck_word(word: str) -> bool:
    open_parenthesis = 0
    for i in word:
        if i == "(":
            open_parenthesis += 1
        elif i == ")":
            open_parenthesis -= 1
            
    if open_parenthesis == 0:
        return True
    else:
        return False

