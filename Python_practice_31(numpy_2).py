import numpy as np
from numpy.linalg import matrix_power,cholesky

def non_zero_elements(some_list):
    # индексы ненулевых элементов
    return np.nonzero(some_list)

def create_2d_random_array(x_size, y_size):
    # создаёт двумерный массив из рандомных элементов
    return np.random.random((y_size, x_size))

def create_random_array(min, max, length):
    # Создаёт массив из рандомных элементов от "min" до "max" длиной length
    return np.random.randint(min, max, length)

def find_max_and_min(some_list):
    # найти минимальный и максимальный элемент
    return some_list.min(), some_list.max()

def find_arifmetical_mean(some_list):
    # найти среднее арифметическое массива
    return some_list.mean()

def create_matrix_diagonal(a, b):
    # Создать A^2 матрицу с числами от "a" до "b" под диагональю
    return np.diag(np.arrange(a, b), k=-1)

def multyplying_2_arrays(list_1, list_2):
    # Перемножение двух матриц
    return np.dot(list_1, list_2)

def inverse_range_of_values(some_list, a, b):
    # Меняет знак в диапазоне значений от "a" до "b"
    some_list[(a < some_list) & (some_list <= b)] *= -1

def sort_for_highest(some_list):
    # Возвращает отсортированный массив от малого и большому элементы
    return np.sort(some_list)

