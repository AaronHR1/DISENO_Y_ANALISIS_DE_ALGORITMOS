arreglo=[-9,3,5,-2,9,-7,4 ,8 , 6 ]
productoMaximo=0
index1=-1
index2=-1

for i in range(len(arreglo)):
    for j in range(i+1,len(arreglo)):
        if abs(arreglo[i]*arreglo[j]) > productoMaximo:
            productoMaximo=arreglo[i]*arreglo[j]
            index1=i
            index2=j


print("los dos numeros con el producto mas grande son:")
print(arreglo[index1], arreglo[index2])

