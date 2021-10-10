def thesaurus(*names):
    my_dict = dict()
    for i in names:
        my_dict.setdefault(i[0], [])
        my_dict[i[0]].append(i)
    return my_dict

print(thesaurus("Илья", "Иван", "Петр", "Мария"))