src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [num for k, num in enumerate(src) if num > src[k - 1] and k != 0]
print(my_list)
