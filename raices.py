import cmath
A=float(input("Ingrese término cuadrático   "))
B=float(input("Ingrese término lineal  "))
C=float(input("Ingrese término independiente  "))
raiz=cmath.sqrt((B**2)-(4*A*C))
#print(raiz)
root1=(-B+raiz)/(2*A)
print(root1)
root2=(-B-raiz)/(2*A)
print(root2)
