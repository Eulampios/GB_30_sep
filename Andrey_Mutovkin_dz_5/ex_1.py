def odd_int(value):
    k = 1
    while k <= value:
        yield k
        k += 2

print(list(odd_int(5)))
