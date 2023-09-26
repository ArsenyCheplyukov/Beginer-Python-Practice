#Выведите все элементы, которые меньше 5

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_than_five_1(some_list):
    print([elem for elem in some_list if elem < 5])

def less_than_five_2(some_list):
    print(list(filter(lambda elem: elem < 5, some_list)))

def less_than_five_3(some_list): 
    for elem in some_list:
        if elem < 5:
            print(elem)

less_than_five_1(nums)
less_than_five_2(nums)
less_than_five_3(nums)
