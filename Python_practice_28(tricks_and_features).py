import datetime
import itertools
from collections import Counter
from collections import OrderedDict

# Присвоение первого непустого значения из ряда
# X = A or B or C or None
# X = A or default

# Назначение переменных и функций по условию (тернарный оператор)
# A = Y if X else Z - можно использовать функции вместо "X" и "Z"

# Нумерованные списки
for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)
# Или при помощи второго элемента задающего начальное значение
for i, item in enumerate(['a', 'b', 'c'], 1):
    print(i, item)

# Сортировка словаря по значениям
d = {'яблоки':40, 'апельсины':80, 'бананы':70}
print(sorted(d, key=d.get))

# Генераторы словарей и множеств
S = {i**2 for i in range(10)}
D = {i: i**2 for i in range(10)}
print(S)
print(D)

# Нахождение наиболее часто повторяющихся элементов списка
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(a), key=a.count))
# Или
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
cnt = Counter(a)
print(cnt.most_common(3))

# Вывод при помощи print
for part in ["prog", "lib", ".io", "\n"]:
    print(part, end='')

# Вывод значения по умолчанию для отсутствующего ключа словаря
d = {'a':1, 'b':2}
print(d.get('c'))
print(d.get('c', 3))

# Удаление дубликатов в списке
items = [2, 2, 3, 3, 1]
print(list(set(items)))
# Или 
print(list(OrderedDict.fromkeys(items).keys()))

# Транспонирование двумерного массива данных
original = [('a', 'b'), ('c', 'd'), ('e', 'f')]
transposed = zip(*original)
print(list(transposed))

# Проверка на анаграммность
str1 = 'proglib'
str2 = 'prgolib'
print(Counter(str1) == Counter(str2))

# Объединение списков без цикла
L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(list(itertools.chain.from_iterable(L)))
# или
L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(sum(L, []))

# Объединение строк
numbers = [1, 2, 3, 4, 5]
print(', '.join(map(str, numbers)))

# Распаковывание последовательностей при неизвестном числе элементов
seq = [1, 2, 3, 4]
*a, b, c = seq
print(a, b, c)

# Обмен значений при помощи кортежей
a, b = 1, 2
print(a, b)

