import string
import operator
import re
from file import File
from cesar import shift, cesar

def decode_cesar(file):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 
                'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
    f = File('/home/klenlen/уМИРЭАй/7_семестр/Инф.Без./ciper_Cesar/tolstoi_l_n__voina_i_mir.txt')
    f.open_file()

    # Сздается эталонная таблица частоты встречаемости букв
    w_and_p_freq = frequency_analysis(alphabet, f.text)

    # Сздается таблица частоты встречаемости зашифрованных букв
    encode_text_freq = frequency_analysis(alphabet, file.text)

    # Замена букв по таблицам
    sub_decode_text = substitution(alphabet, w_and_p_freq, encode_text_freq, file.text)
    print(sub_decode_text)

    # Словарь совпавших букв
    good_letters = coincidence(sub_decode_text, file.text)

    # Поиск нужного сдвига
    step = steper(good_letters, alphabet)
    print(f'\nсдвиг на {step}\n')


    decode_alph = shift(alphabet, step)
    file.write_to_file(cesar(alphabet, decode_alph, file.text))

def steper(letters, alphabet):
    """Ищет ключ по алфавиту в зависимости от растояния между совпавшими буквами"""

    l = []
    for k, v in letters.items():
        shift = 0
        for let in alphabet:
            if k == let:
                shift = 1
            elif v == let:
                l.append(shift)
                continue
            else:
                shift += 1
    dic = {}
    for i in l:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic.update({i: 1})
    c = 0
    sh = 0
    for key, val in dic.items():
        if val > c:
            c = val
            sh = key
    return sh

def coincidence(txt_1, txt_3):
    """Проверяет совпадение между двумя текстами"""

    f2 = File('/home/klenlen/уМИРЭАй/7_семестр/Инф.Без./ciper_Cesar/copy.txt')
    f2.open_file()
    txt_2 = f2.text
    c = {}
    coinc_let = {}
    for i in range(len(txt_1)):
        if txt_1[i] == txt_2[i]:
            if txt_1[i] not in c.keys() and txt_1[i].lower() not in c.keys() and txt_1[i].upper() not in c.keys():
                c.update({txt_1[i].lower(): txt_3[i].lower()})
    for k,v in c.items():
        if k != v:
            coinc_let.update({k: v})
    # print(f'\nсовпали буквы: {coinc_let}')
    return coinc_let

def substitution(alpha, base, encode, text):
    """Заменяет буквы в зашиврованном тексте относительно эталонной таблице частоты букв и таблицы зашиврованного текста"""

    txt = ''
    for letter in text:
        if letter in alpha:
            for i, (key, freq) in enumerate(base):
                if encode[i][0] == letter:
                    txt += base[i][0]
        elif letter.lower() in alpha:
            for i, (key, freq) in enumerate(base):
                if encode[i][0] == letter.lower():
                    txt += base[i][0].upper()
        else:
            txt += letter
    return txt

def frequency_analysis(alphabet, text):
    """Возвращет список пар (буква: частота встречаемости в тексте)"""

    frequency = {}
    for letter in alphabet:
        counter = len(re.findall(letter, text))
        frequency.update({letter: counter/len(text)})
    # [print(c) for c in sorted(frequency.items(), key=operator.itemgetter(1))]
    return sorted(frequency.items(), key=operator.itemgetter(1))

if __name__ == '__main__':
    f = File('/home/klenlen/уМИРЭАй/7_семестр/Инф.Без./ciper_Cesar/file.txt')
    f.open_file()
    text = f.text
    decode_cesar(f)
