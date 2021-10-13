import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def jokes(num):
    '''функция будет генерировать шуктку из 3 слов, используя 3 словаря
    :param num: введите количество слов
    :return: Вы, все-таки, увидите шутку ☻'''
    joke_list = []
    for i in range(num):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        joke_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return joke_list


print(jokes(4))
print(jokes(3))
