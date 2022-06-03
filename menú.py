#creacion del menú
#iniciamos creando una variable para que el usuario pueda escribir su nombre para que comiense.
#y crear una variable para que el usuario escoga si quiere o no juar el juego.

from modulefinder import IMPORT_NAME
import random
import time

nombre = int(input("digite su nombre:_"))
print(f"bienvenido {nombre} espero que estes bien")
print("presiona 1 si acepta el reto y 2 si no quieres jugar ")
respuesta = int(input("digite su respuesta:_"))

if respuesta == 1:
    print("exelente comenzemos el juego")
if respuesta == 2:
    print("lo lamento ya sera en otro momento")
else:
    print("lo lamento eso no esta dentro de los parametro del juego")
    
respuestas2 = input("digite ")    
print("""se bienvenido nuevamente a este grandioso juego que hemos preparado para ti este juego consta de 9 juegos sea de adivinansa, creacion o jugar contra el computador puedes escoger cualquiera de las opciones 
      
      1) matriz aleatorio
      2) matriz cuadrada 1,5
      3) creacion y sumatoria de la matriz
      4) juego de las 3 rayas
      5) solucion de ecuaciones lineales
      6) ecuaciones cuadraticas
      7) la frase
      8) registros
      9) juego del ahorcado""")     

respuestas2 = input("digite su respuesta")
    
if respuestas2 == 1:
    print("comenzemos el juego")  

j = int(input(" ingrese las columnas:_ "))
a = int(input(" ingrese las filas:_ "))
m = []

for i in range(j):
    ma = []
    for i in range(a):
        li = random.randint(0,10)
        ma.append(li)
    m.append(ma)
    
for o in m:
    print(o)
       
from collections import Counter

l = o
c = Counter(l)
print("El numero que mas se repitio fue")
print(max(c, key=c.get))
    
# 2) Segundo punto
if respuestas2 == 2:
    print("continuemos el juego")
    
from unicodedata import ucd_3_2_0

m = []
sum1 = 0
sum2 = 0
cont = 1

a = int(input("ingrese dimensión cuadrada"))

def crear():
    for i in range(a):
        ma = []
        for i in range(a):
            l = random.randint(1,5)
            ma.append(l)
        m.append(ma)
    return m
       
def izquierda (a,m):
    mul1 = 1
    for i in range(a):
        for u in range(a):
            if i==u:
                mul1 = mul1*m[i][u]
                
    return mul1

def derecha (a,m):
    cont= a-1
    mul2 = 1
    for i in range(a):
        mul2 = mul2*m[i][cont]
        cont = cont-1
        
    return mul2

def mostrar(m):
    print("----------------------------------------")
    for i in m:
        print(i)
           
while 5 > 2:
    m = []
    m = crear()
    mostrar(m)
    a = len(m)
    v1 = izquierda(a,m)
    v2 = derecha(a,m)
    
    if v1 == v2:
        print("----------------------------------------------------------")
        print(f"Las dos variables {v1} y {v2} son iguales ")
        print("Fueron necesarios ",cont," intentos para cumplir la condición")
        break
    else:
        cont = cont+1
        
#3) creacion y sumatoria de la matriz
if respuestas2 == 3:
    print("continuemos el juego")
matriz = []
lista = []
for i in range(2):
    lista= [input("digite el numero:_") for j in range(2)]    
    matriz.append(lista)
print(matriz)  
# creamos una variable llamdas suma para la sumatoria de la lista y la matriz 
suma = matriz + lista 
#en esta parte se ponen si es un cuadro magico o no
if lista == matriz:
    print(f"es un cuadro magico, el resulktado es: {suma}")
if lista != matriz:
    print(f"no un cuadro magico, el resulktado es: {suma}")
    
#4) juego de las 3 rayas
if respuestas2 == 4:
    print("continuemos el juego")
    
import random

def drawBoard(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("'¿Quieres ser X u O?'")
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain(): 
    print("¿Quieres volver a jugar? (sí o no)")
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):
    
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("¿Cuál es tu próximo movimiento? (1-9)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5
    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("Bienvenido a Tic Tac Toe!")

while True:
    
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("El"  + turn + ' ira primero.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("'¡Hurra! Has ganado el juego")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("El juego es un empate")
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("¡La computadora te ha vencido! Has perdido.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('¡El juego es un empate!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
    
#5) solucion de ecuaciones lineales
if respuestas2 == 6:
    print("contunuemos con el juego") 
    
def sistema_ecuaciones_2x2 (a, b, c, d, e, f):
    determinante = a*e-b*d
    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f -c*d) / determinante
        return x, y
    
    else:
        return None, None

print('digite los valores para a, b, c, d, e, f: ')
a, b, c, d, e, f = map(float, input().split())
print(sistema_ecuaciones_2x2(a, b, c, d, e, f))

#sistema de ecuaciones 3x3 

# gx + hy + iz = j
# kx + ly + mz = n
# ox + py + qz = r

def sistema_ecuaciones_2x2 (g, h, i, j, k, l, m, n, o, p, q, r):
    determinante = []
    if determinante != 0:
        x = () / determinante
        y = () / determinante
        return x, y
    
    else:
        return None, None

print('digite los valores para g, h, i, j, k, l, m, n, o, p, q, r: ')
g, h, i, j, k, l, m, n, o, p, q, r = map(float, input().split())
print(sistema_ecuaciones_2x2(g, h, i, j, k, l, m, n, o, p, q, r))


#6) ecuaciones cuadraticas
if respuestas2 == 6:
    print("comenzemos el juego") 
 
from math import sqrt

# mostramos un mensaje de bienvenida
print('¡Hola! Vamos a resolver una ecuación de segundo grado:')
print('    ax² + bx + c = 0\n')

# pedimos los coeficientes al usuario
a, b, c = [float(input(f'Dame el coeficiente {coef}: ')) for coef in ('a', 'b', 'c')]

# calculamos el discriminante
discriminante =  b * b - 4 * a * c

if discriminante < 0: # comprobamos si no existen soluciones reales
    print(f'La ecuación no tiene soluciones reales.')
else:
    raiz = sqrt(discriminante)      # calculamos la raíz
    x_1 = (-b + raiz) / (2 * a)     # calculamos una primera solución
    if discriminante != 0:          # comprobamos si hay otra solución
        x_2 = (-b - raiz) / (2 * a) # calculamos la segunda solución
        print(f'Las soluciones son {x_1} y {x_2}.') # mostramos las dos soluciones
    else:
        print(f'La única solución es x = {x_1}') # mostramos la única solución   
    
#7) la frase
if respuestas2 == 7:
    print("juego no encontrado") 
#8) registros 
if respuestas2 == 8:
    print("juego no encontrado") 


#9) juego del ahorcado      
# Listas de Palabras
 
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
          