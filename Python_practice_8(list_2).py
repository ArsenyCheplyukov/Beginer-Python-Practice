#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.


list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def sorting_for_simmilar_1(some_list_1, some_list_2):
    result = []
    for index_1 in some_list_1:
        for index in some_list_2:
            result.append(index)
    return result

def sorting_for_simmilar_2(some_list_1, some_list_2):
    return list(filter(lambda elem: elem in some_list_1, some_list_2))

def sorting_for_simmilar_3(some_list_1, some_list_2):
    return [elem for elem in some_list_1 if elem in some_list_2]

def printing(list):
    for i in range(len(list)):
        print(list[i])

result_1 = sorting_for_simmilar_1(list_1, list_2)
result_2 = sorting_for_simmilar_1(list_1, list_2)
result_3 = sorting_for_simmilar_3(list_1, list_2)

printing(result_1)
printing(result_2)
printing(result_3)