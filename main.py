import numpy as np

list = ['a','b','c','d','e','f','g']
list2 = [1,2,3,4,5,6,7,8,9]
list3 = [1.0,3.14,12.5,125.0,12.5]

a = np.array(list3)

# Tipo
print(type(a))

# Acceder a un elemento
print(a[0])

# Conocer el tipo de dato del array
print(a.dtype)

# Conocer el tamaño
print(a.size)

# Conocer el numero de dimensiones del arreglo
print(a.ndim)

# OPERACIONES EN NUMPY

# Adicion de Vectores
u = np.array([1,0])
v = np.array([0,1])
z = u+v
print(type(z))
print(z)

# Resta de Vectores
u = np.array([1,0])
v = np.array([0,1])
z = u-v
print(type(z))
print(z)

# Multiplicacion por un escalar
y = np.array([1,2])
z = 2*y
print(type(z))
print(z)

# Multiplicacion de vectores
u = np.array([1,2])
v = np.array([3,2])
z = u*v
print(type(z))
print(z)

# Producto Punto ( 1*3 + 2*1 )
u = np.array([1,2])
v = np.array([3,1])
resultado = np.dot(u,v)
print(type(resultado))
print(resultado)

# Suma de vector + escalar
u = np.array([1,2,3,-1])
z = u+1
print(type(z))
print(z)

# FUNCIONES UNIVERSALES

