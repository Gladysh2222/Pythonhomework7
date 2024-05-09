"""ВСЕ функции"""


import random

MAX_LEN = 7
MIN_LEN = 4
MIN_LETTER = ord('a')
MAX_LETTER = ord('z')
VOWELS = {'a','o','y','i','u','e'}


def generate_name_file(filename: str, count_name: int):
    """Генерация псевдоимен."""
    with open(filename, 'w', encoding='utf-8') as f:
        for j in range(count_name):
            len_name = random.randint(MIN_LEN, MAX_LEN)
            name = []
            for i in range(len_name):
                name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
            has_vowels = False
            for letter in name:
                if letter in VOWELS:
                    has_vowels = True
                    break
            if not has_vowels:
                ind = random.randint(0, len_name-1)
                letter = random.choice(list(VOWELS))
                name[ind] = letter
            print(f'{"".join(name).capitalize()}', file=f, end='')
            f.write('\n' if j < count_name - 1 else "")


if __name__ == '__main__':
    generate_name_file("data_names.txt", 25)

    """
Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла,
возвращайтесь в его начало.
"""


def read_line_or_begin(fd) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def process_files(file_numbers, file_names, file_res):
    with open(file_numbers, 'r', encoding='utf-8') as f_num:
        with open(file_names, 'r', encoding='utf-8') as f_names:
            with open(file_res, 'w', encoding='utf-8') as f_res:
                length1 = len(f_num.readlines())
                length2 = len(f_names.readlines())
                length = max(length1, length2)
                for i in range(length):
                    line_num = read_line_or_begin(f_num)
                    line_name = read_line_or_begin(f_names)
                    a, b = line_num.split('|')
                    a = int(a)
                    b = float(b)
                    res = a * b
                    if res < 0:
                        res *= -1
                        line_name = line_name.lower()
                    else:
                        res = round(res)
                        line_name = line_name.upper()
                    f_res.write(f'{line_name} {res}')
                    f_res.write('\n' if i < length - 1 else "")


if __name__ == '__main__':
    process_files('data.txt', 'data_names.txt', 'res.txt')


    """
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
"""
import random
import os

MIN_LETTER = ord('a')
MAX_LETTER = ord('z')

def generate_text(length):
    """Генерирует случайное имя файла."""
    name = []
    for i in range(length):
        name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
    return "".join(name)


def generate_files(extension:str,
                   directory: str,
                   min_length=6,
                   max_length=30,
                   min_bytes=256,
                   max_bytes=4096,
                   num_files=42):
    """Генерирует файлы с заданными параметрами."""
    if not os.path.exists(directory) or not os.path.isdir(directory):
        os.mkdir(directory)
    for i in range(num_files):
        name_length = random.randint(min_length, max_length)
        filename = generate_text(name_length)
        text_length = random.randint(min_bytes, max_bytes)
        text = generate_text(text_length)
        while True:
            try:
                with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
                    f.write(text)
            except:
                filename = generate_text(name_length)
            else:
                break


if __name__ == '__main__':
    generate_files('rnd', 'files')


    """
Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""
from file4 import generate_files

def generate_with_dictionary(dictionary: dict):
    for key, value in dictionary.items():
        generate_files(key, 'files', num_files=value)


if __name__ == '__main__':
    d = {
        'doc': 5,
        'jpg': 10,
        'png': 23,
        'txt': 15,
    }
    generate_with_dictionary(d)



"""
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os

DICTIONARY = {
    'doc': 'texts',
    'txt': 'texts',
    'jpg': 'pictures',
    'png': 'pictures',
}

def sort_files(directory):
    for f in os.listdir(directory):
        extension = f.rsplit('.')[-1]
        if extension not in DICTIONARY:
            continue
        new_directory = f'{directory}/{DICTIONARY[extension]}'
        if not os.path.exists(new_directory) or not os.path.isdir(new_directory):
            os.mkdir(new_directory)
        os.rename(f'{directory}/{f}',
                  f'{new_directory}/{f}')


if __name__ == '__main__':
    sort_files('files')