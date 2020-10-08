import random
import re
from file import File

def cesar(file):
    step = random.randint(-32, 32)
    print(f'\nсдвиг на {step}\n')
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 
                'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
    encode_alph = shift(alphabet, step)
    # print(alphabet)
    # print(encode_alph)
    encode_text = text_shift(alphabet, encode_alph, file.text)
    file.write_to_file(encode_text)
    # print(file.open_file())

def text_shift(alph, code, txt):
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
    lst = ls.copy()
    if step < 0:
        step = abs(step)
        for _ in range(step):
            lst.append(lst.pop(0))
    else:
        for _ in range(step):
            lst.insert(0, lst.pop())
    return lst

if __name__ == '__main__':
    f = File('/home/klenlen/уМИРЭАй/7_семестр/Инф.Без./ciper_Cesar/file.txt')
    f.open_file()
    cesar(f)