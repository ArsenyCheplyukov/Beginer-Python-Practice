import numpy as np
from numpy.linalg import matrix_power
from numpy.linalg import cholesky

def transformation_lst(ints_as_strings):
    ints = map(int, ints_as_strings)
    lst = list(ints)
    return lst

def find_unique(some_list):
    return len(some_list) == len(set(some_list))

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
e = np.array([[1,-2j],[2j,5]])
f = np.arrange(10,50)
z = z[::-1]
print(z)
print(a)
b = np.linspace(0, 2, 9)
print(b)
c = np.random.random_sample((3, 2))
print(c)
d = np.random.uniform(2, 8, (2, 10))
print(d)
np.random.shuffle(d)
print(d)
print(matrix_power(a, 2))
print(np.linalg.cholesky(np.matrix(e)))

