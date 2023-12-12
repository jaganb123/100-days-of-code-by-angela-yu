def infiniteGen():
    i = 1
    while True:
        yield i
        i += 1

gen = infiniteGen()
for _ in range(100):
    print(next(gen))
