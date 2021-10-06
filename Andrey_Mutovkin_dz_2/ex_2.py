s_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
          'была', '+5', 'градусов']

new_list = []
for i in s_list:
    if i.isdigit():
        new_list.extend(['"', f'{int(i):02}', '"'])
    elif (i.startswith('+') or i.startswith('-')) and i[1:].isdigit():
        new_list.extend(['"', f'{i[0]}{int(i[1:]):02}', '"'])
    else:
        new_list.append(i)

tot = ' '.join(new_list)
print(tot)

char_ind = []
for ind, letter in enumerate(tot):
    if letter == '"':
        char_ind.append(ind)

for ind in range(len(char_ind)):
    if ind % 2 == 0:
        char_ind[ind] = char_ind[ind] + 1
    else:
        char_ind[ind] = char_ind[ind] - 1

for del_ind in reversed(char_ind):
    tot = tot[:del_ind] + tot[del_ind + 1:]