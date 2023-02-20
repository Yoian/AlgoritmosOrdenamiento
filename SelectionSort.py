from random import randrange

def selectionSort(array):
    for i in range(len(array)):

        idxDes = i
        for j in range(i+1,len(array)):
            if array[idxDes]>array[j]:
                idxDes = j

        array[i],array[idxDes]=array[idxDes],array[i]


lista = [randrange(1,300,8) for i in range(10)]

if __name__ == "__main__":    
    print("La lista desordenada se ve asi",lista)
    selectionSort(lista)
    print("La lista ordenada se ve asi",lista)
