matriz = []
lista = []
for i in range(2):
    lista= [input("digite el numero:_") for j in range(2)]    
    matriz.append(lista)
print(matriz)  

# creamos una variable llamdas suma para la sumatoria de la lista y la matriz 
suma = matriz + lista 

#4 en esta parte se ponen si es un cuadro magico o no
if lista == matriz:
    print(f"es un cuadro magico, el resulktado es: {suma}")
if lista != matriz:
    print(f"no un cuadro magico, el resulktado es: {suma}")

    
