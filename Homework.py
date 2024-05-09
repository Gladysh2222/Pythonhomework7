"""Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.

b. принимать параметр количество цифр в порядковом номере.

c. принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.

d. принимать параметр расширение конечного файла.

e. принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. 
Далее счётчик файлов и расширение."""


import os

def group_rename_files(desired_name, num_digits, original_extension, new_extension, name_range=None):
    counter = 1
    for filename in os.listdir('.'):
        if filename.endswith(original_extension):
            original_name = filename[:name_range[1]] if name_range else filename
            extension = filename.split('.')[-1]
            if original_extension == extension:
                new_name = f"{original_name}_{desired_name}{counter:0{num_digits}}.{new_extension}"
                os.rename(filename, new_name)
                counter += 1
                
# Пример использования:
group_rename_files("newfile", 2, ".txt", "doc", (3, 6))