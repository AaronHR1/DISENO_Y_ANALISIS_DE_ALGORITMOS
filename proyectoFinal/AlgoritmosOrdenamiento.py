import random;
import time;


def algoritmosOrdenamiento(n):
    tiempos=[]
    arreglo=[random.randint(0,1000) for _ in range(n)] 
    
    inicio = time.perf_counter()
    bubbleSort(arreglo.copy())
    fin = time.perf_counter()
    tiempos.append(fin-inicio)

    
    inicio = time.perf_counter()
    mergeSort(arreglo.copy())
    fin = time.perf_counter()
    tiempos.append(fin-inicio)

    inicio = time.perf_counter()
    selecitonSort(arreglo.copy())
    fin = time.perf_counter()
    tiempos.append(fin-inicio)

    tiempos.append(bogoSort(arreglo.copy()))
    
    return tiempos

def mergeSort(arreglo):
    if len(arreglo) <=1:
        return arreglo
    
    mid=len(arreglo)//2
    left=arreglo[:mid]
    right=arreglo[mid:]
    
    leftSorted=mergeSort(left)
    rightSorted=mergeSort(right)
    
    return merge(leftSorted,rightSorted)
           
def merge(left,right):
    sorted=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
        
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

def bubbleSort(arreglo):
    n=len(arreglo)
    for i in range(n):
        for j in range(0,n-i-1):
           if(arreglo[j]>arreglo[j+1]):
               arreglo[j],arreglo[j+1]=arreglo[j+1],arreglo[j]
       
def selecitonSort(arreglo):
    n=len(arreglo)
    for i in range(n):
        menor=i
        for j in range(i,n):
            if arreglo[j]<arreglo[menor]:
                menor=j

        arreglo[menor],arreglo[i]= arreglo[i],arreglo[menor]
               
def bogoSort(arreglo):
    inicio = time.perf_counter()
    def estaOrdenado(a):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False
        return True

    
    while not estaOrdenado(arreglo):
        if time.perf_counter() - inicio > 10:
            return None
        random.shuffle(arreglo)


print(algoritmosOrdenamiento(10000))