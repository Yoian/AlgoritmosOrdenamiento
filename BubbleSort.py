#1.- Comenzar a hacer comparaciones de elementos adyacentes
#2.- Repetir hasta tener una pasada completa sin ningún swap
from random import randint,randrange

def bubbleSort(array):
    n = len(array)
    
    for i in range(n):

        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)

lista = [randrange(1,300,8) for i in range(5)]

print("La lista desordenada se ve asi",lista)
bubbleSort(lista)
print("La lista ordenada se ve asi",lista)