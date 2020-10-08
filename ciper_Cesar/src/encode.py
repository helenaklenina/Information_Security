import random
from file import File
from cesar import cesar, shift

def encoding(file):
    step = random.randint(-32, 32)
    print(f'\nсдвиг на {step}\n')
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 
                'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
    encode_alph = shift(alphabet, step)
    encode_text = cesar(alphabet, encode_alph, file.text)
    file.write_to_file(encode_text)

if __name__ == '__main__':
    f = File('/home/klenlen/уМИРЭАй/7_семестр/Инф.Без./ciper_Cesar/file.txt')
    f.open_file()
    encoding(f)