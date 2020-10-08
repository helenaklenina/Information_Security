import re

def cesar(alph, code, txt):
    """Сдвиг каждой буквы текста относительно сдвига алфавита"""

    text = ''
    for letter in txt:
        try:
            if letter.isupper():
                id = code[alph.index(letter.lower())].upper()
            else:
                id = code[alph.index(letter)]
            text += id
        except ValueError:
            text += letter
    return text

def shift(ls, step):
    """Сдвиг букв алфавита по ключу - step"""

    lst = ls.copy()
    if step < 0:
        step = abs(step)
        for _ in range(step):
            lst.append(lst.pop(0))
    else:
        for _ in range(step):
            lst.insert(0, lst.pop())
    return lst

