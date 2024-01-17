import os
import random

def clearScreen():
    sistema_operativo = os.name
    if sistema_operativo == 'posix':
        os.system('clear')
    elif sistema_operativo == 'nt':
        os.system('cls')

prompt_historial = []
lives_character = 3
sword_usos = 4 


def addText(texto):
    prompt_historial.append(texto)

    if len(prompt_historial) > 8:
        prompt_historial.pop(0)

def showPrompt():
    if prompt_historial:
        print("Últimas acciones:")
        for prompt in prompt_historial:
            print("->" + " " + prompt)
    else:
        print("Aún no hay acciones")

def find_link(map, symbol):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == symbol:
                return i, j

def print_map(map):
    for x in map:
        print(' '.join(x))

def move_character(map, position, direccion):
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
        return False

    if 0 <= new_position[0] < len(map) and 0 <= new_position[1] < len(map[0]):
        if map[new_position[0]][new_position[1]] not in ['#', 'O', 'T', 'C', 'S1?', 'M', 'F', '1', 'E9', '0', '~', '*']:
            map[position[0]][position[1]] = ' '
            map[new_position[0]][new_position[1]] = 'X'
            return True
    
    return False

def special_symbols(map, new_position):
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = new_position[0] + i
            column = new_position[1] + j
            if 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'C':
                addText("Puedes cocinar aquí")  
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'T':
                addText("Puedes golpear este árbol")
                hit_tree(map, new_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'E1':
                attack_enemy(map, new_position)

def hit_tree(map, new_position):
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = new_position[0] + i
            column = new_position[1] + j   
            if 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'T':
                hit = input("¿Quieres golpear este árbol?: ")                               
                if hit.lower() == 'yes':
                    probability = random.randint(1, 10)
                    
                    if probability in [1, 2, 3, 4]:
                        addText('Obtuviste una manzana')
                    elif probability == 5:
                        addText('Obtuviste una espada')
                    else:
                        addText('No obtuviste nada')

def attack_enemy(map, position):
    global sword_usos  # Número máximo de usos de la espada
    global lives_character

    for i in range(-1, 2):
        for j in range(-1, 2):
            row = position[0] + i
            column = position[1] + j
            if 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'E1':
                attack = input("¿Quieres atacar al enemigo?: ")
                if attack.lower() == 'attack':
                    if sword_usos > 0:
                        sword_usos -= 1  # Reducir los usos de la espada

                        # Extracting the numeric part from the enemy representation
                        enemy_life = int(''.join(filter(str.isdigit, map[row][column])))

                        # Decreasing the enemy's life
                        enemy_life -= 1

                        # Updating the map with the new enemy life
                        map[row][column] = f'E{enemy_life}'

                        addText('¡Valiente, sigue luchando Link!')

                        if enemy_life == 0:
                            addText('Derrotaste a un enemigo, esta zona es peligrosa.')
                            map[row][column] = '  '  # El enemigo desaparece al llegar a 0 de vida
                    else:
                        addText('Tu espada está gastada. Encuentra otra.')

                    # El enemigo ataca al personaje
                    if lives_character > 0:
                        lives_character -= 1
                        addText(f'Ten cuidado Link, solo te quedan {lives_character} vidas')
                    else:
                        addText('¡Game Over!')

def move_enemy(map, row, column):
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random_move = random.choice(possible_moves)
    
    new_row = row + random_move[0]
    new_column = column + random_move[1]

    if 0 <= new_row < len(map) and 0 <= new_column < len(map[0]) and map[new_row][new_column] == ' ':
        map[new_row][new_column] = 'E1'
        map[row][column] = ' '
    else:
        # Si la nueva posición no es válida, el enemigo no se mueve
        pass

def check_nearby_element(map, position, element):
    # Verificar si está cerca del elemento en las posiciones adyacentes
    for i in range(position[0] - 1, position[0] + 2):
        for j in range(position[1] - 1, position[1] + 2):
            if 0 <= i < len(map) and 0 <= j < len(map[0]) and map[i][j] == element:
                return (i, j)  # Devolver las coordenadas del elemento
    return None

def interactuar_santuario(map, character_position):
    global lives_character  # Declarar vida_personaje como global

    santuario_position = check_nearby_element(map, character_position, 'S1?')
    if santuario_position:
        # Incrementar la vida
        lives_character += 1
        # Actualizar el mapa
        map[santuario_position[0]][santuario_position[1]] = 'S1 '
        # Mensaje
        addText(f"Has encontrado un santuario, tu vida ha aumentado. Ahora tienes {lives_character} vidas.")

def show_map(map_zelda):
    clearScreen()
    print(map_zelda)

foxlist = [" ", "F"]
fox_spawn = random.choice(foxlist)

map = [   ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', 'O', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', '~', 'O', 'O', 'O', 'O', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '*'],
          ['*', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', '', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S0?', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', 'O', 'O', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S1?', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', 'M', ' ', ' ', ' ', ' ', ' ', ' ', f'{fox_spawn}', ' ', ' ', ' *'],
          ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*']]

map_zelda = ("""
* Map * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                         *                   *
*   Hyrule         S0                     Death mountain  *                   *
*                                 S2?                     *                   *
*         S1?                                      S3?    *                   *
*                                                         *                   *
*                            Castle                       *                   *
*                                                         *                   *
*                     S4                              S5  *                   *
*  Gerudo                              S6?       Necluda  *                   *
*                                                         *                   *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

character_position = find_link(map, 'X')

while True:
    clearScreen()
    print("* Hyrule  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print_map(map)
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    showPrompt()
    direction = input("\n¿Hacia dónde quieres ir? (W, A, S, D): ")

    if direction.lower() == 'show map':
        addText(direction)
        while True:
            show_map(map_zelda)
            showPrompt()
            back = input("Escribe 'back' para regresar: ")
            if back.lower() == "back":
                addText(back)
                break  # Salir del bucle interno
            else:
                addText("Entrada no válida. Intenta de nuevo.")

    if direction.lower() == 'exit':
        break

    if move_character(map, character_position, direction.lower()):
        character_position = find_link(map, 'X')
        if direction.lower() == "w":
            addText("Te has movido hacia arriba")
            special_symbols(map, character_position)
        elif direction.lower() == "a":
            addText("Te has movido hacia la izquierda")
            special_symbols(map, character_position)
        elif direction.lower() == "s":
            addText("Te has movido hacia abajo")
            special_symbols(map, character_position)
        elif direction.lower() == "d":
            addText("Te has movido hacia la derecha")
            special_symbols(map, character_position)

    else:
        addText("No puedes moverte en esa dirección o has alcanzado el límite del mapa.")

print("Juego terminado.")
