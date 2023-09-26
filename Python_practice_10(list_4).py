# Напишите программу для слияния нескольких словарей в один.

num = 3

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

def addition(*a):
    result = {}
    result.update(a)
    return result

print((addition(dict_a, dict_b, dict_c)).items())