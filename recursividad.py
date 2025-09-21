import math

def sumaRecursiva(arreglo,suma=0):
    if len(arreglo) ==0 :
        return suma
    
    suma+=arreglo.pop(0) 
    return sumaRecursiva(arreglo,suma)


def contarDigitos(entero,digitos=0):
   
    if(entero <10):
        return digitos+1
    digitos+=1
    
    return contarDigitos(entero/10,digitos)


def eliminarElementoMedio(pila,index=0):

    elementoActual=pila.pop()
     
    if not pila:
        pila.append(elementoActual)
        return math.ceil(index/2)
    

    mitad=eliminarElementoMedio(pila,index+1)
    
    if index != mitad:
        pila.append(elementoActual)

    return mitad

def inversa(cadena,index):
    
    if index==len(cadena): return ""
    caracterActual=cadena[index]
    resto=inversa(cadena,index+1)

    return resto + caracterActual


def verificarPalindromo(cadena):
    if cadena==inversa(cadena,0):
        return True
    else:
        return False
    




