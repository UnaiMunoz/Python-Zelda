import os
import random
import mysql.connector
from ascii import menu_cocina
conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')


cursor = conexion.cursor()
def clearScreen():
    sistema_operativo = os.name
    if sistema_operativo == 'posix':
        os.system('clear')
    elif sistema_operativo == 'nt':
        os.system('cls')
clearScreen()
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
        if map[new_position[0]][new_position[1]] not in ['#', 'O', 'T', 'C', 'S1?',  'S1 ', 'S0?', 'S0 ', 'M', 'F', '1', 'E9', '0', '~', '*','E1']:
            map[position[0]][position[1]] = ' '
            map[new_position[0]][new_position[1]] = 'X'
            return True
    
    return False


def cook(cooking):
    if cooking.lower() == "salad":
        addText("You selected Salad")
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining - 2
        WHERE food_name = 'Apple' AND quantity_remaining >= 2;""")
        if cursor.rowcount == 0:
            addText("You can't cook that! Not enough 'Apple' available.")
        else:
        #AÑADIR ENSALADA
            cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining + 1
            WHERE food_name = 'Salad';""")
        #PESCADO
    elif cooking.lower() == "pescatarian":
        addText("You selected Pescatarian")
        cursor.execute("""
            SELECT
                (SELECT quantity_remaining FROM game_food WHERE food_name = 'Apple' AND quantity_remaining >= 1) AS check_manzanas,
                (SELECT quantity_remaining FROM game_food WHERE food_name = 'pescao' AND quantity_remaining >= 1) AS check_pescado;
        """)
        check_comida = cursor.fetchone()
        check_manzanas = check_comida[0]
        check_pescado = check_comida[1]
        
        if check_manzanas is not None and check_manzanas >= 1 and check_pescado is not None and check_pescado >= 1:
            cursor.execute("""
                UPDATE game_food
                SET quantity_remaining = quantity_remaining - 1
                WHERE food_name IN ('pescao', 'Apple') AND quantity_remaining >= 1;
            """)
            
            cursor.execute("""
                UPDATE game_food
                SET quantity_remaining = quantity_remaining + 1
                WHERE food_name = 'pescatarian';
            """)
        else:
            addText("You can't cook that! Not enough 'Apple' or 'Fish' available.")

        #ROASTED
    elif cooking.lower() == "roasted":
        addText("You selected roasted")
        cursor.execute("""
            SELECT
                (SELECT quantity_remaining FROM game_food WHERE food_name = 'Apple' AND quantity_remaining >= 1) AS check_manzanas,
                (SELECT quantity_remaining FROM game_food WHERE food_name = 'meat' AND quantity_remaining >= 1) AS check_meat;
        """)
        check_comida = cursor.fetchone()
        check_manzanas = check_comida[0]
        check_carne = check_comida[1]
        
        if check_manzanas is not None and check_manzanas >= 1 and check_carne is not None and check_carne >= 1:
            cursor.execute("""
                UPDATE game_food
                SET quantity_remaining = quantity_remaining - 1
                WHERE food_name IN ('Meat', 'Apple') AND quantity_remaining >= 1;
            """)
            
            cursor.execute("""
                UPDATE game_food
                SET quantity_remaining = quantity_remaining + 1
                WHERE food_name = 'roasted';
            """)
        else:
            addText("You can't cook that! Not enough 'Apple' or 'Meat' available.")
        addText("You cant cook that!!!")


def pescar():
    while True:
        clearScreen()
        print("* Hyrule  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print_map(map)
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print_map(inventario)

        showPrompt()

        cocinando = input("¿Quieres pescar? (s/n): ")
        if cocinando.lower() == "s":
            addText("Estás pescando.")
            showPrompt()
            probability = random.randint(1, 10) 
            if probability in [1, 2]:
                obtener_pescao()
            else:
                addText('No has pescado nada')

        elif cocinando.lower() == "n":
            addText("Decidiste no pescar.")
            break
        else:
            addText("Entrada no válida. Por favor, responde con 's' o 'n'.")
            showPrompt()

def special_symbols(map, new_position):
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = new_position[0] + i
            column = new_position[1] + j
            if 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'C':
                opcioncocina = input("Quieres cocinar? (yes/exit): ")
                while opcioncocina == "yes":
                    clearScreen()
                    print(menu_cocina)
                    addText("You're cooking!")
                    showPrompt()
                    cooking = input("What do you wanna cook?(Salad/Pescatarian/Roasted)")
                    cook(cooking)
                    opcioncocina = input("Quieres cocinar? (yes/No): ")
                    print(menu_cocina)
                if opcioncocina.lower() =="exit":
                    addText("You're no longer cooking")
                    break
                else:
                    addText("This receipt isn't available or you wrote an incorrect order")
                    opcioncocina = input("Quieres cocinar? (yes/No): ")
                    clearScreen()
                    addText("You're cooking again!")
                    print(menu_cocina)
                    showPrompt()
                    cooking = input("What do you wanna cook?(Salad/Pescatarian/Roasted)")
                    cook(cooking)                    
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'T':
                addText("Puedes golpear este árbol")
                hit_tree(map, new_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'E1':
                attack_enemy(map, new_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'S0?':
                interactuar_santuario0(map, character_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'S1?':
                interactuar_santuario1(map, character_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == '~':
                pescar()


def obtener_manzana():
    cursor.execute("""
    UPDATE game_food
    SET quantity_remaining = quantity_remaining + 1
    WHERE food_name = 'Apple';""")
    conexion.commit()
    addText('Obtuviste una manzana')

def obtener_pescao():
    cursor.execute("""
    UPDATE game_food
    SET quantity_remaining = quantity_remaining + 1
    WHERE food_name = 'pescao';""")
    conexion.commit()
    addText('Has pescado un pez')



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
                        obtener_manzana()
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

def interactuar_santuario0(map, character_position):
    global lives_character  # Declarar vida_personaje como global

    santuario_position = check_nearby_element(map, character_position, 'S0?')
    if santuario_position:
        # Incrementar la vida
        lives_character += 1
        # Actualizar el mapa
        map[santuario_position[0]][santuario_position[1]] = 'S0 '
        # Mensaje
        addText(f"Has encontrado un santuario, tu vida ha aumentado. Ahora tienes {lives_character} vidas.")

def interactuar_santuario1(map, character_position):
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


def vida_total():
    cursor.execute("""
        SELECT max_hearts FROM game
    """)
    corazones_totales = cursor.fetchone()
    if corazones_totales:
        return corazones_totales[0]
    else:
        return 0


def vida():
    cursor.execute("""
        SELECT hearts_remaining FROM game
    """)
    corazones = cursor.fetchone()
    if corazones:
        return corazones[0]
    else:
        return 0
def vegetal():
    from inventory import vegetables
def armas():
    cursor.execute("""
    SELECT COUNT(weapon_name) AS total_quantity
FROM game_weapons; 
    """)
    contar = cursor.fetchone()
    if contar:
        return contar[0]
    else:
        return 0
def blood_moon():
    cursor.execute("""
        SELECT blood_moon_countdown FROM game;
    """)
    lunaroja = cursor.fetchone()
    if lunaroja:
        return lunaroja[0]
    else:
        return 0
def contar_comida():
    cursor.execute("""SELECT SUM(quantity_remaining) AS total_quantity
FROM game_food;""")
    comida = cursor.fetchone()
    if comida:
        return comida[0]
    else:
        return 0

def espada(cursor):
    cursor.execute("""
    SELECT quantity_remaining FROM game_weapons
    WHERE weapon_name = 'Sword'
    """)
    result = cursor.fetchone()
    return result[0] if result else None  # Return the quantity or None if no result

def escudo(cursor):
    cursor.execute("""
    SELECT quantity_remaining FROM game_weapons
    WHERE weapon_name = 'Shield'
    """)
    result = cursor.fetchone()
    return result[0] if result else None

inventario = (f"""
* * * * * Inventory *
*                   *
* Link        ♥ {vida()}/{vida_total()} *
* Blood moon in {blood_moon()}  *
*                   *
* Equipment         *
*   Sword: {espada(cursor)}        * 
*   Shield: {escudo(cursor)}       *
*                   *
* Food:     {contar_comida()}       *
* Weapons:  {armas()}       *
* * * * * * * * * * *


""")

map = [   ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', 'O', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', '~', 'O', 'O', 'O', 'O', '~', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '*',],
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
                break  
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
conexion.close()
print("Juego terminado.")
