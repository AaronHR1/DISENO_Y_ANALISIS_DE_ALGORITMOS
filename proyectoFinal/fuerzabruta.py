def area_triangulo(a, b,c):
    x1, y1 = a[0],a[1]
    x2, y2 = b[0],b[1]
    x3, y3 = c[0],c[1]
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2

def mayor_triangulo_bruteforce(puntos):
    maxArea = -1
    mejor = (None, None, None)

    n = len(puntos)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                area = area_triangulo(puntos[i], puntos[j], puntos[k])
                if area > maxArea:
                    maxArea = area
                    mejor = (puntos[i], puntos[j], puntos[k])

    return maxArea, mejor
