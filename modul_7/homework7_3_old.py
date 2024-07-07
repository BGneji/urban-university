file_name = 'text_7_3_old.txt'
# открытие файла
with open(file_name, mode='r', encoding='utf8') as file:
# чтение файла
    for item in file:
    # вывод данных по строчно
        print(item, end='')

# оператор with сам следит за закрытие файла как только закончатся все операции с файлом