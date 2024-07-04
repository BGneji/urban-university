# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
#
# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
# Алгоритм получения словаря такого вида в методе get_all_words:
# Создайте пустой словарь all_words.
# Переберите названия файлов и открывайте каждый из них, используя оператор with.
# Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
# (тире обособлено пробелами, это не дефис в слове).
# Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
#
# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
#
# for name, words in get_all_words().items():
#   # Логика методов find или count
#
# Пример результата выполнения программы:
# Представим, что файл 'test_file.txt' содержит следующий текст:
#
#
# Пример выполнения программы:
# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего
#
# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def info(self):
        print(self.file_names)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                words = file.read().split()
                wordsqq = self.symbol_del(words)
                for i in wordsqq:
                    if file.name not in all_words:
                        all_words[file.name] = []
                        all_words[file.name].append(i.lower())
                    else:
                        all_words[file.name].append(i.lower())
            return all_words

    def find(self, word):
        d = {}
        word = word.lower()
        text = self.get_all_words()
        for key, value in text.items():
            try:
                d[key] = (value.index(word) + 1)
                return d
            except ValueError:
                return 'Такого слова нет'

    def count(self, count_word):
        d_count = {}
        count_word = count_word.lower()
        text = self.get_all_words()
        for key, value in text.items():
            d_count[key] = value.count(count_word)
            return d_count

    def symbol_del(self, list_):
        """Убираем символы из слов"""
        l = []
        translator = str.maketrans('', '', ",,.=!?;: - ")
        for word in list_:
            clean_word = word.translate(translator)
            l.append(clean_word)
        return l


f1 = 'file1.txt'
f2 = 'file2.txt'

# a = WordsFinder(f2)
# # a.info()
# print(a.get_all_words())
# print(a.find('text'))
# print(a.count('TeXt'))



# Поисковое слово: 'captain'
#
# Код:
#
finder1 = WordsFinder(f2)
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
#
# Результат:
#
# {'Walt Whitman - O Captain! My Captain!.txt': ['o', 'captain', 'my', 'captain', 'o', 'captain', 'my', 'captain', 'our', 'fearful', 'trip', 'is', 'done', 'the', 'ship', 'has', 'weather’d', 'every', 'rack', 'the', 'prize', 'we', 'sought', 'is', 'won', 'the', 'port', 'is', 'near', 'the', 'bells', 'i', 'hear', 'the', 'people', 'all', 'exulting', 'while', 'follow', 'eyes', 'the', 'steady', 'keel', 'the', 'vessel', 'grim', 'and', 'daring', 'but', 'o', 'heart', 'heart', 'heart', 'o', 'the', 'bleeding', 'drops', 'of', 'red', 'where', 'on', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'o', 'captain', 'my', 'captain', 'rise', 'up', 'and', 'hear', 'the', 'bells', 'rise', 'up', '—', 'for', 'you', 'the', 'flag', 'is', 'flung', '—', 'for', 'you', 'the', 'bugle', 'trills', 'for', 'you', 'bouquets', 'and', 'ribbon’d', 'wreaths', '—', 'for', 'you', 'the', 'shores', 'acrowding', 'for', 'you', 'they', 'call', 'the', 'swaying', 'mass', 'their', 'eager', 'faces', 'turning', 'here', 'captain', 'dear', 'father', 'this', 'arm', 'beneath', 'your', 'head', 'it', 'is', 'some', 'dream', 'that', 'on', 'the', 'deck', 'you’ve', 'fallen', 'cold', 'and', 'dead', 'my', 'captain', 'does', 'not', 'answer', 'his', 'lips', 'are', 'pale', 'and', 'still', 'my', 'father', 'does', 'not', 'feel', 'my', 'arm', 'he', 'has', 'no', 'pulse', 'nor', 'will', 'the', 'ship', 'is', 'anchor’d', 'safe', 'and', 'sound', 'its', 'voyage', 'closed', 'and', 'done', 'from', 'fearful', 'trip', 'the', 'victor', 'ship', 'comes', 'in', 'with', 'object', 'won', 'exult', 'o', 'shores', 'and', 'ring', 'o', 'bells', 'but', 'i', 'with', 'mournful', 'tread', 'walk', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'walt', 'whitman']}
# {'Walt Whitman - O Captain! My Captain!.txt': 2}
# {'Walt Whitman - O Captain! My Captain!.txt': 10}
