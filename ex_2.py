eng_rus = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate_adv(eng_word):
    if eng_word[0] == eng_word[0].upper():
        eng_word = eng_word.lower()
        return eng_rus[eng_word].capitalize()
    else:
        return eng_rus[eng_word]

print(num_translate_adv('Five'))
print(num_translate_adv('five'))
print(num_translate_adv('one'))
print(num_translate_adv('One'))