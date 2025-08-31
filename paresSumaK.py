def solucionArreglos(arreglo,k):
    soluciones=0

    for i in range(len(arreglo)):
        for j in range(i,len(arreglo)):
            if arreglo[i]+arreglo[j]==k:
                print("solucion encontrada en el par:")
                print(f"{arreglo[i]} en la posición: {i}")
                print(f"{arreglo[j]} en la posición: {j}")
                soluciones+=1
    
    if soluciones==0:
        print("Solucion no encontrada")
    
    return soluciones 

def solucionHash(arreglo, k):
    diccionario = {}
    soluciones=0

    for i in range(len(arreglo)):
        complemento=k-arreglo[i]
        if complemento in diccionario:
            print("solucion encontrada en el par:")
            print(f"{arreglo[i]} en la posición: {i}")
            print(f"{complemento} en la posición: {diccionario[complemento]}")
            soluciones+=1
        else:
            diccionario[arreglo[i]]=i
    
    if soluciones==0:
        print("Solucion no encontrada")
    
    return soluciones 


