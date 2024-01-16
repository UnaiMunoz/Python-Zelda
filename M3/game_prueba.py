import os

def clearScreen():
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

def find_link(map, symbol):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == symbol:
                return i, j

def print_map(map):
    for x in map:
        print(' '.join(x))
    print()

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
        if map[new_position[0]][new_position[1]] not in ['#', 'O', 'T', 'C', 'E', 'S', 'M', 'F', '1', '9', '0', '~']:
            map[position[0]][position[1]] = ' '
            map[new_position[0]][new_position[1]] = 'X'
            return True

    return False


def obtener_position_personaje(map, symbol):
    return find_link(map, symbol)

map =  [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', 'O'],
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

character_position = find_link(map, 'X')

while True:
    clearScreen()
    print_map(map)
    showPrompt()
    direction = input("\nWhere you want to go? (W,A,S,D): ")

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
    else:
        addText("You cannot move in that direction or you have reached the limit of the map.")

print("Game finished.")
