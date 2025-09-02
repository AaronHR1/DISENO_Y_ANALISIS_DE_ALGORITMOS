def busquedaLineal(arreglo,k):
    comparaciones=0
    for i in range(len(arreglo)):
        if arreglo[i]==k:
            print("valor encontrado en el index:" + str(comparaciones))
            return comparaciones+1
        else:
            comparaciones+=1
    
    return None

print(busquedaLineal([3,4,5,3,4,5,3,4,5,3,4,5,9,4,5,],9))