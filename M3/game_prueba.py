import os
import random
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
        if map[new_position[0]][new_position[1]] not in ['#', 'O', 'T', 'C', 'E', 'S', 'M', 'F', '1', '9', '0', '~', '*']:
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
                    addText("You can cook here")  
                elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'T':
                    addText("You can hit this tree")
                    hit_tree(map, new_position)
                elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'E1':
                    addText("")
                    hit_tree(map, new_position)



def hit_tree(map, new_position):
         for i in range(-1, 2):
            for j in range(-1, 2):
                row = new_position[0] + i
                column = new_position[1] + j   
                if 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'T':
                                hit = input("Wanna hit this tree?: ")                               
                                if hit.lower() == 'yes':
                                    probabilidad = random.randint(1, 10)
                                    
                                    if probabilidad in [1, 2, 3, 4]:
                                        addText('You obtained an apple')
                                    elif probabilidad == 5:
                                        addText('You obtained a sword')
                                    else:
                                        addText('You obtained nothing')

foxlist = [" ", "F"]
fox_spawn = random.choice(foxlist)

map =  [  ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', 'O', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', '~', 'O', 'O', 'O', 'O', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', 'O', 'O', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S1?', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', 'M', ' ', ' ', ' ', ' ', ' ', ' ', f'{fox_spawn}', ' ', ' ', ' *'],
          ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*']]



character_position = find_link(map, 'X')

while True:
    clearScreen()
    print_map(map)
    showPrompt()
    direction = input("\nWhere you want to go? (W,A,S,D): ")

    if direction.lower() == 'exit':
        break

    if move_character(map, character_position, direction.lower()):
        character_position = find_link(map, 'X')
        if direction.lower() == "w":
            addText("You have moved up")
            special_symbols(map,character_position)
        elif direction.lower() == "a":
            addText("You have moved left")
            special_symbols(map,character_position)
        elif direction.lower() == "s":
            addText("You have moved down")
            special_symbols(map,character_position)
        elif direction.lower() == "d":
            addText("You have moved right")
            special_symbols(map,character_position)

    else:
        addText("You cannot move in that direction or you have reached the limit of the map.")

print("Game finished.")
