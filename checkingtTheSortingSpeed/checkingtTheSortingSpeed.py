import random
import time
from random import shuffle

def SortInsert(listArray): 
    for i in range(len(listArray)):
        j = i - 1
        element = listArray[i]
        while listArray[j] > element and j >= 0:
            listArray[j + 1] = listArray[j]
            j -= 1
        listArray[j + 1] = element
    return listArray

def QuickSort(listArray, l, n):
    i, j = l, n
    p = listArray[(n + i) >> 1]
    while i <= j:
        while  listArray[i] < p:
            i += 1
        while  listArray[j] > p:
            j -= 1
        if i <= j:   
            listArray[j], listArray[i] = listArray[i], listArray[j]
            j -= 1
            i += 1
    if j > l:    
        QuickSort(listArray, l, j)        
    if n > i:
        QuickSort(listArray, i, n)              
    return listArray

def SuffeledList(listSuffed, SIZE):
    listSuffed = []
    for i in range(SIZE):
        listSuffed.append(i)
    random.shuffle(listSuffed)     
    return listSuffed

def RandomFloatsIntegers(listRandomfloatInt, SIZE, a, b, randomAct):# randomAct- выбор для random
    listRandomfloatInt = []
    for i in range(SIZE):
        listRandomfloatInt.append(randomAct(a, b))    
    return listRandomfloatInt

def compsort(listArray):
    if listArray == sorted(listArray):
        return "OK" 
    return "Fail"

def test(size, a, b, selector, listArray):
    if selector:
        start = time.clock()
        listArray = SortInsert(listArray)
        print("time SortInsert:",time.clock() - start)
        return compsort(listArray)
    else:
        start = time.clock()
        listArray = QuickSort(listArray, 0, size - 1)
        print("time QuickSort:",time.clock() - start)
        return compsort(listArray)
    
listArray = []    
size, a, b = 10000, 5, 1000 # a,b - диапазон

if __name__ == "__main__":

    listArray = RandomFloatsIntegers(listArray, size, a, b, random.uniform)
    print("Status uniform SortInsert: %s" % test(size, a, b, 1, listArray))
    listArray = RandomFloatsIntegers(listArray, size, a, b, random.uniform)      
    print("Status uniform QuickSort : %s" % test(size, a, b, 0, listArray))
    listArray = RandomFloatsIntegers(listArray, size, a, b, random.randint)
    print("Status randint SortInsert: %s" % test(size, a, b, 1, listArray))
    listArray = RandomFloatsIntegers(listArray, size, a, b, random.randint)      
    print("Status randint QuickSort : %s" % test(size, a, b, 0, listArray))
    listArray = SuffeledList(listArray, size)
    print("Status shuffle SortInsert: %s" % test(size, a, b, 1, listArray))
    listArray = SuffeledList(listArray, size)     
    print("Status shuffle QuickSort : %s" % test(size, a, b, 0, listArray))
          
