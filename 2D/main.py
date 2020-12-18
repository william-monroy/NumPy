import numpy as np

#********************************************************************************
#                                                                               *
#                     ARRAYS EN NUMPY DE 2 DIMENSIONES                          *
#                                                                               *
#********************************************************************************

a = [[11,12,13],[21,22,23],[31,32,33]]

A = np.array(a)
print(type(A))
print(A)

print('Dimensiones:',A.ndim)
print('De:',A.shape)
print('Tamaño:',A.size)

# Slicing
print('A[0:2,2] = ',A[0:2,2])

# Suma de Arrays
X = np.array([[1,0],[0,1]])
Y = np.array([[2,1],[1,2]])
Z = X + Y
print('Suma:')
print(Z)

# Multilicacion de Array por un escalar
Y = np.array([[2,1],[1,2]])
Z = 2 * Y
print('array*2:')
print(Z)

# Multiplicacion de Array por Array
X = np.array([[1,0],[0,1]])
Y = np.array([[2,1],[1,2]])
Z = X * Y
print('array_A*array_B:')
print(Z)

# Multiplicacion de matrices
A = np.array([0,1,1],[1,0,1])
print(A.rows)
B = np.array([1,1],[1,1],[-1,1])
print(B.size)
C = np.dot(A,B)
print(C)

