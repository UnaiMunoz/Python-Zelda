import os

def limpiar_pantalla():
    sistema_operativo = os.name
    if sistema_operativo == 'posix':
        os.system('clear')  # Comando para limpiar la pantalla en sistemas Unix
    elif sistema_operativo == 'nt':
        os.system('cls')    # Comando para limpiar la pantalla en sistemas Windows

prompt_historial = []

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

def encontrar_personaje(mapa, simbolo):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == simbolo:
                return i, j

def imprimir_mapa(mapa):
    for fila in mapa:
        print(' '.join(fila))
    print()

def mover_personaje(mapa, posicion, direccion):
    nueva_posicion = list(posicion)

    if direccion == 'w' and nueva_posicion[0] > 0:
        nueva_posicion[0] -= 1
    elif direccion == 's' and nueva_posicion[0] < len(mapa) - 1:
        nueva_posicion[0] += 1
    elif direccion == 'a' and nueva_posicion[1] > 0:
        nueva_posicion[1] -= 1
    elif direccion == 'd' and nueva_posicion[1] < len(mapa[0]) - 1:
        nueva_posicion[1] += 1
    else:
        print("No puedes moverte en esa dirección.")
        return False

    if 0 <= nueva_posicion[0] < len(mapa) and 0 <= nueva_posicion[1] < len(mapa[0]):
        if mapa[nueva_posicion[0]][nueva_posicion[1]] not in ['#', 'O', 'T', 'C', 'E', 'S', 'M', 'F', '1', '9', '0', '~']:
            mapa[posicion[0]][posicion[1]] = ' '
            mapa[nueva_posicion[0]][nueva_posicion[1]] = 'X'
            return True

    print("No puedes moverte en esa dirección o has llegado al límite del mapa.")
    return False


def obtener_posicion_personaje(mapa, simbolo):
    return encontrar_personaje(mapa, simbolo)

mapa = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', 'O'],
        [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', '~', 'O', 'O', 'O', 'O', '~'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~',' ~', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~'],
        [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', '9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
        [' ', 'O', 'O', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', 'M', ' ', ' ', ' ', 'F', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']
]

posicion_personaje = encontrar_personaje(mapa, 'X')

while True:
    limpiar_pantalla()
    imprimir_mapa(mapa)
    showPrompt()
    direccion = input("\nIngresa la dirección (W,A,S,D): ")

    if direccion.lower() == 'salir':
        break

    if mover_personaje(mapa, posicion_personaje, direccion.lower()):
        posicion_personaje = encontrar_personaje(mapa, 'X')
        if direccion.lower() == "w":
            addText("Te has movido hacia arriba")
        elif direccion.lower() == "a":
            addText("Te has movido hacia la izquierda")
        elif direccion.lower() == "s":
            addText("Te has movido hacia abajo")
        elif direccion.lower() == "d":
            addText("Te has movido hacia la derecha")
    else:
        addText("No puedes moverte en esa dirección o has llegado al límite del mapa.")

print("Juego terminado.")
