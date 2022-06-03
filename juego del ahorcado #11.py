import random
import time

## Listas de Palabras
 
palabras_de_informatica = [ "sitemas", "bases de datos", "informatica","sofware", "telefono","computadora", "programacion", "inteligencia artificial,","sitios web", "python", "java", "javascript","html", "css","usb",
                "mouse","teclado","monitor", "pc", "ram", "robotica", "consola", "videojuegos", "visual estudios", "codigo", "back end", "front end", "libreria", "bug" , "full stack"]

nombres_de_paises = ["colombia","brasil","alemania","argentina","ecuador","venexuela","panama","mexico","bolivia","chile","japon","china", "españa","francia","corea del nonrte"]

print("Bienvenido al juego de ahorcado")
time.sleep(2)
print("El objetivo del juego es adivinar la palabra secreta letra por letra")
print("tienes 5 vidas, pierdes una vida cada que te equivocas si te quedas sin vidas pierdes")
time.sleep(2)

print("Desea jugar con palabras de que son objetos informaticos ")
time.sleep(2)
 
cat_seleccionada = input("Ingrese 1 para objetos informaticos y 2 para nombres de paises: ")
 
while True:
    if cat_seleccionada.lower() == "1":
        print("excelente a seleccionado la informatica")
        palabra_secreta = random.choice(palabras_de_informatica)
        break
    elif cat_seleccionada.lower() == "2":
        print("excelente a seleccionado a los paises del mundo")
        palabra_secreta = random.choice(nombres_de_paises)
        break
 
    else:
        print("Por favor seleccione una categoria valida")
        cat_seleccionada = input("Ingrese 1 para objetos informaticos y 2 para nombres los nombres de los paise ")
        
 ## Es el numero de veces que se puede eqivocar
vidas = 5
 
lista_letras_adivinadas = []
 
## Imprimimos la palabra sin letras
print('_' * len(palabra_secreta))

while True:
     
    while True:
        letra_adivinada = input("Adivina una letra: ")
        if(len(letra_adivinada)!=1 and letra_adivinada.isnumeric()):
            print("Eso no es una letra intenta con una sola letra")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                print("Ya habias intentado con esa letra intenta con otra por favor")
            else:
                lista_letras_adivinadas.append(letra_adivinada)
 
                if letra_adivinada.lower() in palabra_secreta:
                    print("Felicidades adivinaste una letra")
                    break
                else:
                    vidas = vidas-1
                    print("Te haz equivocado y perdido una vida")
                    print("Te quedan " + str(vidas) + " vidas")
                    break 
    if vidas==0:
     print("Haz perdido la palabra secreta era: "+ palabra_secreta)
     
    estatus_actual = ""
 
    letras_faltantes = 0
    for letra in palabra_secreta:
 
 
        if letra in lista_letras_adivinadas:
            estatus_actual = estatus_actual + letra
 
        else:
            estatus_actual = estatus_actual + "_"
            letras_faltantes = letras_faltantes + 1
 
    ## Imprimir palabra con algunas letras
    print(estatus_actual)
 
 
    if letras_faltantes == 0:
        print("Felicidades haz ganado")
        print("La palabra secreta es: " + palabra_secreta) 
