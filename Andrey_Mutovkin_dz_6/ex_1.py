from statistics import mode  # Импортируем функцию mode() для нахождения самого частого значения

ip_adress_list = []  # список из IP-адресов для поиска спамера
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for i in file_1:
        res = i.split()
        remote_addr, _, _, _, _, request_type, requested_resource, *_ = res
        final = (remote_addr, request_type, requested_resource)
        print(final)  # Ответ на первое задание
        '''Решение первого задания под звездочкой.
        Решал через создание нового списка. Наверняка можно было список не создавать,
        чтобы не грузить память, но не додумался'''
        ip_adress_list.append(remote_addr)
    print('IP-адрес спамера: ', mode(ip_adress_list))  # находим часто встречающийся IP-адрес функцией mode()
    print('Количество запросов спамера: ',
          ip_adress_list.count(mode(ip_adress_list)))  # считаем сколько раз в списке встречается
