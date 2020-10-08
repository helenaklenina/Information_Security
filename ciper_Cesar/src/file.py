import re
import random

class File:
    """Класс для файлов"""
    text = ''

    def __init__(self, file):
        self.file = file

    def open_file(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            self.text = f.read()
            return self.text

    def write_to_file(self, text):
        with open(self.file, 'w') as f:
            f.write(text)

    def find_random_part(self):
        """Нахождение случайной главы для шифрования"""
        chapters = re.findall('[IVX]+\.', self.text)
        print(chapters)
        text = self.text.split(' ')
        from_here = random.randint(0, len(chapters))
        to_here = from_here + 1
        print(f"from here {from_here} is {chapters[from_here]} to here {to_here} is {chapters[to_here]}")
        c = 0
        for word in text:
            # print(word)
            # chapters[]
            if word in chapters:
                print(word, c)
                c += 1
                if c == from_here:
                    print('\n\n')
                    print(c)
                    print('\n\n')
                    chapter = chapter + word
                    if word == to_here and word is chapters[to_here]:
                        print(chapter)
                        self.text = chapter
                        break
