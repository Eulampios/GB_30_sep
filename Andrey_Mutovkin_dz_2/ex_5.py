list = [23.34, 4.51, 87, 23, 55.6, 45, 91.35, 54, 741, 251, 342, 345, 65, 44, 5, 55, 9]
for i in list:
    rub = int(i)
    kop = (i - int(i)) * 100
    print(f'{rub} руб {kop:02.0f} коп')

list = [23.34, 4.51, 87, 23, 55.6, 45, 91.35, 54, 741, 251, 342, 345, 65, 44, 5, 55, 9]
print(id(list))
list.sort()
print(id(list))
for i in list:
    rub = int(i)
    kop = (i - int(i)) * 100
    print(f'{rub} руб {kop:02.0f} коп')

list = [23.34, 4.51, 87, 23, 55.6, 45, 91.35, 54, 741, 251, 342, 345, 65, 44, 5, 55, 9]
for k in sorted(list)[::-1][:5]:
    rub = int(k)
    kop = (k - int(k)) * 100
    print(f'{rub} руб {kop:02.0f} коп')

print([f'{int(k)} руб {(k - int(k)) * 100:02.0f} коп' for k in sorted(list)[::-1][:5]])
