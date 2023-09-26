import operator

# Отсортируйте словарь по значению в порядке возрастания и убывания.

maximum_index = 4

list_1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

list_2 = dict(sorted(list_1.items(), key=operator.itemgetter(1), reverse=True))
list_3 = dict(sorted(list_1.items(), key=operator.itemgetter(1)))

for item in list_2.items():
    print(item)

for item in list_3.items():
    print(item)
