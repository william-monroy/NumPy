import matplotlib.pyplot as plt
import numpy as np
import time 
import sys

#--------------------------------------------------------------------

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

#--------------------------------------------------------------------


#********************************************************************************
#                                                                               *
#                           ARRAYS EN 1 DIMENSION                               *
#                                                                               *
#********************************************************************************

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = [1.0, 3.14, 12.5, 125.0, 12.5]

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
u = np.array([1, 0])
v = np.array([0, 1])
z = u+v
print(type(z))
print(z)

#Plotvec1(u, z, v)

# Resta de Vectores
u = np.array([1, 0])
v = np.array([0, 1])
z = u-v
print(type(z))
print(z)

# Multiplicacion por un escalar
y = np.array([1, 2])
z = 2*y
print(type(z))
print(z)

# Multiplicacion de vectores
u = np.array([1, 2])
v = np.array([3, 2])
z = u*v
print(type(z))
print(z)

# Producto Punto ( 1*3 + 2*1 )
u = np.array([1, 2])
v = np.array([3, 1])
resultado = np.dot(u, v)
print(type(resultado))
print(resultado)

# Suma de vector + escalar
u = np.array([1, 2, 3, -1])
z = u+1
print(type(z))
print(z)

# FUNCIONES UNIVERSALES

# Promedio
a = np.array([1, -1, 1, -1])
prom = a.mean()
print(type(prom))
print(prom)

# Mayor valor de un array
b = np.array([1, -2, 3, 4, 5])
max_valor = b.max()
print(type(max_valor))
print(max_valor)

# Menor valor de un array
b = np.array([1, -2, 3, 4, 5])
min_valor = b.min()
print(type(min_valor))
print(min_valor)

# Crear arrays con pi
print(np.pi)
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)  # Sacamos el seno a cada elemento de x
print(type(y))
print(y)

# GRAFICAR FUNCIONES MATEMATICAS

# Linspace = Crear arrays con linspace(inicio,fin,num = numero_de_elementos)
ejm = np.linspace(-2, 2, num=5)
print(ejm)
ejm = np.linspace(-2, 2, num=9)
print(ejm)

# Uso de matplotlib
x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)

plt.plot(x, y)  # Crear la grafica
plt.show()  # Mostrar la grafica

