import random
import os
import ascii
import time
import mysql.connector
conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')
cursor = conexion.cursor()

def clearScreen():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':  # Para sistemas basados en Unix/Linux/Mac
        os.system('clear')
    elif sistema_operativo == 'nt':  # Para sistemas Windows
        os.system('cls')

prompt_historial = []


def get_name():
    cursor.execute("""
        SELECT user_name FROM game
        where game_id = (SELECT MAX(game_id) FROM game);
    """)
    nombre = cursor.fetchone()
    if nombre:
        return nombre[0]
    else:
        return 0

def menu():
    import zelda_menu

def addText(texto):
    prompt_historial.append(texto)

    if len(prompt_historial) > 8:
        prompt_historial.pop(0)

def showPrompt():
    if prompt_historial:
        print("Latest actions: ")
        for prompt in prompt_historial:
            print("->" + " " + prompt)
    else:
        print("There are no actions yet")
# Función para imprimir la matriz en el prompt
def imprimir_matriz(matriz):
    for fila in matriz:
        print(''.join(fila))

def encontrar_personaje(mapa, simbolo):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == simbolo:
                return i, j

vidas_ganon = 8
vidas_link = 9

ganonlist = ["Ganon is powerful, are you sure you can defeat him?",
"Ganon's strength is supernatural, Zelda fought with bravery.",
"To Ganon, you are like a fly, find a weak spot and attack.",
"Ganon will not surrender easily.",
"Ganon has fought great battles, is an expert fighter.",
"Link, transform your fears into strengths.",
"Keep it up, Link, Ganon can't hold out much longer.",
"Link, history repeats itself, Ganon can be defeated.",
"Think of all the warriors who have tried before.",
"You fight for the weaker ones, Link, persevere."]

ganonsentences = random.choice(ganonlist)

def mover_personaje(mapa, posicion, direccion):
    global vidas_ganon
    global vidas_link
    nueva_posicion = list(posicion)

    if direccion == 'd' and nueva_posicion[1] < len(mapa[0]) - 1:
        nueva_posicion[1] += 1
    elif direccion == 'a' and nueva_posicion[1] > 0:
        nueva_posicion[1] -= 1


    if 0 <= nueva_posicion[0] < len(mapa) and 0 <= nueva_posicion[1] < len(mapa[0]):
        if mapa[nueva_posicion[0]][nueva_posicion[1]] == '\\':  # Corregido aquí
            atacar_dragon = input("¡Te encuentras cerca de Ganon!! Escribe 'attack' para atacar: ").lower()
            if atacar_dragon.lower() == 'attack':
                vidas_ganon -= 1
                vidas_link -= 1
                addText(f"{ganonsentences}")
                addText(f"Keep fighting {get_name()}, ganon has only {vidas_ganon} lives left")
                addText(f"Ganon attacks you back! Careful {get_name()}, you lost one life,you have only {vidas_link} left")                
                # Actualiza las vidas del dragón y realiza otras acciones necesarias.
        elif mapa[nueva_posicion[0]][nueva_posicion[1]] not in ['#', 'O', 'T', 'C', 'E', 'S', 'M', 'F', '\\']:
            mapa[posicion[0]][posicion[1]] = ' '
            mapa[nueva_posicion[0]][nueva_posicion[1]] = 'X'

            return True

    else:
        addText("No puedes moverte en esa dirección.")
        return False

# Matriz del juego
mapa = [['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ','*'],
          ['*', ' ', ' ', ' ', '\\', '|', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', '*'],
          ['*', ' ', ' ', '', '--', 'o', '--', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' *'],                 
          ['*', ' ', ' ', ' ', '/', '|', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' *'],                
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '>', ' ', ' ', 'v', '-', 'v', '-', 'v', '-', 'v', ' ', ' ', ' ', '|', '>', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' *'],                
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ',', ' ', ' ', '/', '_', '\\', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '/', '_', '\\ ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '', ' *'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\\', '_', '/', '|', ' ', ' ', '|', ' ', '|', "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", '|', ' ', '|', "'", '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' *'],                
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '(', 'q', ' ', 'p', ')', ',', '-', '|', ' ', '|', ' ', '|', '|', ' ', ' ', '_', ' ', ' ', '|', '|', ' ', '|', ' ', '|', ' ', ' ', 'Â·', '_', ' ', ' ', '|', '\\', ' ', ' ', ' ', '', ' *'],
          ['*', 'O', 'T', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '_', '/', '_', '(', '/', '|', ' ', '|', ' ', ' ', ' ', ' ', '|', '#', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ')', ' ', ' ', "'", '-', '/', '/', ' ', ' ', ' ', ' ', ' *'],
          ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' *']
]


posicion_personaje = encontrar_personaje(mapa, 'X')

while True:
    clearScreen()
    print("* Castle  * * * * * * * * * * * * * * * * * * * * * * * *")
    imprimir_matriz(mapa)
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    showPrompt()
    direccion = input(f"\nHacia adelante {get_name()}: ")

    if direccion.lower() == 'salir':
        break

    if mover_personaje(mapa, posicion_personaje, direccion.lower()):
        posicion_personaje = encontrar_personaje(mapa, 'X')
        if direccion.lower() == "d":
            addText("Te has movido hacia la derecha")
        elif direccion.lower() == "a":
            addText("Te has movido hacia la izquierda")
    if vidas_ganon <= 0:
        clearScreen()
        addText("Congrats!You defeated ganon and saved Zelda!!")
        print(f"{ascii.the_end}")
        user_input = input("Wanna return to the menu?")
        if user_input.lower() == "yes":
            clearScreen()
            menu()
        elif user_input.lower() == "no":
            addText("Juego terminado.")
            break
        else:
            addText("This option is not available!")
print("Juego terminado.")