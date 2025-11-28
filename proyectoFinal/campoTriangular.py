with open("campo.in", "r") as f:
    lineas = []
    for linea in f:
        linea = linea.strip()
        if linea != "-1 -1":
            coordenadas=[int(x) for x in linea.split()]
            lineas.append(coordenadas)

ordenadas = sorted(lineas, key=lambda x: (x[0],x[1]))

convexHull1=[]

for i in range(len(ordenadas)):
    convexHull1.append(tuple(ordenadas[i]))
    ch=len(convexHull1)
    
    flag=True
    while flag and ch>=3:
        a=convexHull1[-3]
        b=convexHull1[-2]
        c=convexHull1[-1]
        ab=[a[0]-b[0],a[1]-b[1]]
        ac=[a[0]-c[0],a[1]-c[1]]
        cruz=ab[0]*ac[1]-ab[1]*ac[0]
        if cruz<=0:
            c=convexHull1.pop()
            convexHull1.pop()
            convexHull1.append(c)
            ch=len(convexHull1)
        else: flag=False


ordenadas2 = sorted(lineas, key=lambda x: (-x[0], x[1]))

  
convexHull2=[]    

for i in range(len(ordenadas2)):
    convexHull2.append(tuple(ordenadas2[i]))
    ch=len(convexHull2)
    flag=True
    while flag and ch>=3:
        a=convexHull2[-3]
        b=convexHull2[-2]
        c=convexHull2[-1]
        ab=[a[0]-b[0],a[1]-b[1]]
        ac=[a[0]-c[0],a[1]-c[1]]
        cruz=ab[0]*ac[1]-ab[1]*ac[0]
        if cruz<=0:
            c=convexHull2.pop()
            convexHull2.pop()
            convexHull2.append(c)
            ch=len(convexHull2)
        else: flag=False


convexHullCompleto=set(convexHull1+convexHull2)
convexHullCompleto=list(convexHullCompleto)
print(convexHullCompleto)

            
def area_triangulo(a, b,c):
    x1, y1 = a[0],a[1]
    x2, y2 = b[0],b[1]
    x3, y3 = c[0],c[1]
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2



maxArea=[-1,-1,-1,-1]
n=len(convexHullCompleto)
for i in range(n): 
    for j in range(i+1,n): 
        for k in range(j+1,n): 
           area=area_triangulo(convexHullCompleto[i],convexHullCompleto[j],convexHullCompleto[k])
           if area>=maxArea[0]:
               maxArea=[area,i,j,k]

print(
    "El triangulo de mayor area está formado por: "
    + str(convexHullCompleto[maxArea[1]]) + ", "
    + str(convexHullCompleto[maxArea[2]]) + ", "
    + str(convexHullCompleto[maxArea[3]])
    + " y tiene un area de: "
    + str(maxArea[0])
)
