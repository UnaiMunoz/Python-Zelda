import random
import os

def clearScreen():
    sistema_operativo = os.name
    if sistema_operativo == 'posix':
        os.system('clear')  # Comando para limpiar la pantalla en sistemas Unix
    elif sistema_operativo == 'nt':
        os.system('cls')    # Comando para limpiar la pantalla en sistemas Windows

prompt_historial = []
vida_personaje = 3
vida_enemigo = 1


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
        print("\nThere are no actions yet")

foxlist = [" ", "F"]
fox_spawn = random.choice(foxlist)

map = [   ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', 'O', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', '~', 'O', 'O', 'O', 'O', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', 'O', 'O', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E1', '  ', ' ', ' ', ' ', ' ', ' ', ' ', 'S1?', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', 'M', ' ', ' ', ' ', ' ', ' ', ' ', f'{fox_spawn}', ' ', ' ', '*'],
          ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*']]



def find_link(map, symbol):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == symbol:
                return i, j

def print_map(map):
    for x in map:
        print(' '.join(x))
    

def mover_personaje(map, position, direccion):
    new_position = list(position)

    if direccion == 'w' and new_position[0] > 0:
        new_position[0] -= 1
    elif direccion == 's' and new_position[0] < len(map) - 1:
        new_position[0] += 1
    elif direccion == 'a' and new_position[1] > 0:
        new_position[1] -= 1
    elif direccion == 'd' and new_position[1] < len(map[0]) - 1:
        new_position[1] += 1
    else:
        print("No puedes moverte en esa dirección.")
        return False

    if 0 <= new_position[0] < len(map) and 0 <= new_position[1] < len(map[0]):
        if map[new_position[0]][new_position[1]] not in ['#', 'O', 'T', 'C', 'E1', 'E9', 'M', 'F', 'S1', 'S0', '9', '0', '~', '*']:
            map[position[0]][position[1]] = ' '
            map[new_position[0]][new_position[1]] = 'X'
            return True

    return False


def obtener_position_personaje(map, symbol):
    return find_link(map, symbol)

def check_nearby_element(map, position, element):
    # Verificar si está cerca del elemento en las posiciones adyacentes
    for i in range(position[0] - 1, position[0] + 2):
        for j in range(position[1] - 1, position[1] + 2):
            if 0 <= i < len(map) and 0 <= j < len(map[0]) and map[i][j] == element:
                return (i, j)  # Devolver las coordenadas del elemento
    return None

def interactuar_santuario(map, character_position):
    global vida_personaje  # Declarar vida_personaje como global

    santuario_position = check_nearby_element(map, character_position, 'S1?')
    if santuario_position:
        # Incrementar la vida
        vida_personaje += 1
        # Actualizar el mapa
        map[santuario_position[0]][santuario_position[1]] = 'S1 '
        # Mensaje
        addText(f"Has encontrado un santuario, tu vida ha aumentado. Ahora tienes {vida_personaje} vidas.")


def interactuar_enemigo(map, character_position):
    global vida_personaje
    global vida_enemigo

    enemigo_position = check_nearby_element(map, character_position, 'E')
    if enemigo_position:
        # Realizar el ataque
        # Atacar al enemigo
        vida_enemigo -= 1
        # Reducir la vida del personaje
        vida_personaje -= 1
        # Actualizar el mapa
        map[enemigo_position[0]][enemigo_position[1]] = 'E'
        # Mensaje
        addText("¡Has atacado al enemigo! Tu vida ha disminuido y el enemigo también.")



character_position = find_link(map, 'X')

while True:
    clearScreen()
    print("* Hyrule  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print_map(map)
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    showPrompt()

    santuario_position = check_nearby_element(map, character_position, 'S1?')
    if santuario_position:
        user_input = input(f"\nYou are near a sanctuary! Type 'Open sanctuary' to interact or choose a direction (W, A, S, D): ")
        if user_input.lower() == 'open sanctuary':
            interactuar_santuario(map, character_position)
        else:
            continue

    else:   # Si no está cerca del santuario, solicitar dirección normalmente
        direction = input("\nWhere you want to go? (W, A, S, D): ")

        if direction.lower() == 'salir':
            break

        if mover_personaje(map, character_position, direction.lower()):
            character_position = find_link(map, 'X')
            if direction.lower() == "w":
                addText("You have moved up")
            elif direction.lower() == "a":
                addText("You have moved left")
            elif direction.lower() == "s":
                addText("You have moved down")
            elif direction.lower() == "d":
                addText("You have moved right")

            # Verificar interacciones con el santuario y enemigo después de moverse
            interactuar_enemigo(map, character_position)
        else:
            addText("You cannot move in that direction or you have reached the limit of the map.")

print("Game finished.")


