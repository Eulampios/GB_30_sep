import sys

with open('total.txt', 'w', encoding='utf-8') as tot_file:
    with open('users.csv', encoding='utf-8') as file3:
        line_users = [i.strip() for i in file3]
        with open('hobby.csv', encoding='utf-8') as file5:
            line_hobby = [i.strip() for i in file5]
            my_dict = dict(zip(line_users, line_hobby))
            if len(line_users) > len(line_hobby):
                new_dict = dict.fromkeys(line_users[len(line_hobby):], None)
                my_dict.update(new_dict)
                tot_file.write(str(my_dict))
            elif len(line_users) < len(line_hobby):
                tot_file.write(str(sys.exit(1)))
            else:
                my_dict = dict(zip(line_users, line_hobby))
                tot_file.write(str(my_dict))

