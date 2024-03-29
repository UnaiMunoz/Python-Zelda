import os
import random
import mysql.connector
from ascii import menu_cocina
from ascii import map
import cofres_objetos
conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')

turnos = 0
durabilidad = 4
talado = False
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
        print(''.join(x))

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
        if map[new_position[0]][new_position[1]] not in ['#', 'O', 'T', 'C', 'S3?',  'S3 ', 'S2?', 'S2 ', 'M', 'F', '1', 'E9', '0', '~', '*','E2','t']:
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
        WHERE food_name = 'Apple' AND quantity_remaining >= 2 AND game_id = (SELECT MAX(game_id) FROM game);""")
        if cursor.rowcount == 0:
            addText("You can't cook that! Not enough 'Apple' available.")
        else:
        #AÑADIR ENSALADA
            cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining + 1
            WHERE food_name = 'Salad' AND  game_id = (SELECT MAX(game_id) FROM game);""")
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

pez_pescado = False
def pescar():
    while True:
        global pez_pescado
        clearScreen()
        print("* Death Mountain* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print_map(map)
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        showPrompt()

        if not pez_pescado:  # Verificar si ya se ha pescado un pez en este mapa
            cocinando = input("¿Quieres pescar? (s/n): ")
            if cocinando.lower() == "s":
                addText("Estás pescando.")
                showPrompt()
                probability = random.randint(1, 10) 
                if probability in [1, 2]:
                    obtener_pescao()  # Reemplaza con la implementación real
                    pez_pescado = True  # Marcar que se ha pescado un pez
                else:
                    addText('No has pescado nada')
            elif cocinando.lower() == "n":
                addText("Decidiste no pescar.")
                break
            else:
                addText("Entrada no válida. Por favor, responde con 's' o 'n'.")
                showPrompt()
        else:
            addText("Ya has pescado un pez en este mapa.")
            break


def atacar_zorro(map, position):
    global sword_usos  # Número máximo de usos de la espada
    global lives_character
    zorro_life = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = position[0] + i
            column = position[1] + j
            if 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'F':
                attack = input("¿Quieres atacar al zorro?: ")
                if attack.lower() == 'attack':
                        # Decreasing the enemy's life
                        zorro_life -= 1

                        if zorro_life == 0:
                            addText('Derrotaste al zorro, obtuviste uno de carne.')
                            map[row][column] = '  ' 
                        cursor.execute("""
                            UPDATE game_food
                            SET quantity_remaining = quantity_remaining + 1
                            WHERE game_id = (SELECT MAX(game_id) FROM game) AND food_name = 'Meat';
                        """)
                        conexion.commit()
                        
def swing_sword():
    probabilidad = random.randint(1,10)
    if probabilidad <= 1:
        cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining + 1
            WHERE game_id = (SELECT MAX(game_id) FROM game) AND food_name = 'Meat';
        """)
        addText("¡Atacaste con éxito y mataste a la lagartija!")
        addText("Obtuviste 1 de carne.")
        conexion.commit()
    else:
        addText("You missed")

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
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'E2':
                attack_enemy(map, new_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'S2?':
                interactuar_santuario0(map, character_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'S3?':
                interactuar_santuario1(map, character_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == '~':
                pescar()
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'F':
                atacar_zorro(map, new_position)
            elif 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'M':
                abrir = input("¿Quieres abrir el cofre?: ")
                if abrir.lower() == "yes":
                    objeto_obtenido = cofres_objetos.abrir_cofre("DeathMountain")
                    addText(f"Has obtenido {objeto_obtenido}")
                    map[row][column] = 'W'
                else:
                    addText("Decidiste no abrir el cofre.")

def subir_vida(comida):
    global lives_character
    
    if comida.lower() == "apple":
        if vida() < vida_total():
            cursor.execute("""
                UPDATE game
                SET hearts_remaining = hearts_remaining + 1
                WHERE game_id = (SELECT MAX(game_id) FROM game) AND hearts_remaining < 6;
            """)
            cursor.execute("""
                UPDATE game_food
                SET quantity_remaining = quantity_remaining - 1
                WHERE food_name = 'Apple' AND quantity_remaining >= 1 AND game_id = (SELECT MAX(game_id) FROM game);
            """)
            conexion.commit()
            addText("Has comido una manzana y has subido 1 corazón.")
        else:
            addText("Ya tienes la cantidad máxima de corazones.")
    elif comida.lower() == "salad":
        if vida() < vida_total() - 1:
            cursor.execute("""
                UPDATE game
                SET hearts_remaining = hearts_remaining + 2
                WHERE game_id = (SELECT MAX(game_id) FROM game) AND hearts_remaining < 5;
            """)
            cursor.execute("""
                UPDATE game_food
                SET quantity_remaining = quantity_remaining - 1
                WHERE food_name = 'Salad' AND quantity_remaining >= 1 AND game_id = (SELECT MAX(game_id) FROM game);
            """)
            conexion.commit()
            addText("Has comido una ensalada y has subido 2 corazones.")
        else:
            addText("Ya tienes la cantidad máxima de corazones.")
    elif comida.lower() == "pescatarian":
        if vida() < vida_total() - 2:
            cursor.execute("""
                UPDATE game
                SET hearts_remaining = hearts_remaining + 3
                WHERE game_id = (SELECT MAX(game_id) FROM game) AND hearts_remaining < 4;
            """)
            cursor.execute("""
                UPDATE game_food
                SET quantity_remaining = quantity_remaining - 1
                WHERE food_name = 'Pescatarian' AND quantity_remaining >= 1 AND game_id = (SELECT MAX(game_id) FROM game);
            """)
            conexion.commit()
            addText("Has comido un plato pescatarian y has subido 3 corazones.")
        else:
            addText("Ya tienes la cantidad máxima de corazones.")
    elif comida.lower() == "roasted":
        if vida() < vida_total() - 3:
            cursor.execute("""
                UPDATE game
                SET hearts_remaining = hearts_remaining + 4
                WHERE game_id = (SELECT MAX(game_id) FROM game) AND hearts_remaining < 3;
            """)
            cursor.execute("""
                UPDATE game_food
                SET quantity_remaining = quantity_remaining - 1
                WHERE food_name = 'Roasted' AND quantity_remaining >= 1 AND game_id = (SELECT MAX(game_id) FROM game);
            """)
            conexion.commit()
            addText("Has comido un plato asado y has subido 4 corazones.")
        else:
            addText("Ya tienes la cantidad máxima de corazones.")
    else:
        addText("No puedes comer eso. Intenta con 'eat apple', 'eat salad', 'eat pescatarian' o 'eat roasted'.")

def obtener_manzana():
    try:
        cursor.execute(f"""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining + 1
            WHERE food_name = 'Apple' AND  game_id = (SELECT MAX(game_id) FROM game);
        """)
            
        # Fetch the result before committing
        result = cursor.fetchone()
        
        conexion.commit()
        
        if result:
            addText('Obtuviste una manzana')
    except Exception as e:
        print(f"Error in obtener_manzana: {e}")
        conexion.rollback()  # Rollback the transaction in case of an error


def obtener_pescao():
    cursor.execute("""
    UPDATE game_food
    SET quantity_remaining = quantity_remaining + 1
    WHERE food_name = 'pescao';""")
    conexion.commit()
    addText('Has pescado un pez')

def obtener_espadamadera():
    cursor.execute("""
    UPDATE game_food
    SET quantity_remaining = quantity_remaining + 1
    WHERE food_name = 'wood sword' and game_id = 2;""")
    conexion.commit()
    addText('Obtuviste una espada de madera')

def obtener_escudomadera():
    cursor.execute("""
    UPDATE game_food
    SET quantity_remaining = quantity_remaining + 1
    WHERE food_name = 'wood shield and game_id = 2';""")
    conexion.commit()
    addText('Obtuviste un escudo de madera')

talado = False

def hit_tree(map, new_position, espada_count=1):
    global turnos
    global durabilidad
    global talado

    for i in range(-1, 2):
        for j in range(-1, 2):
            row = new_position[0] + i
            column = new_position[1] + j   

            if 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'T':
                hit = input("¿Quieres golpear este árbol? (yes/no): ").lower()

                if hit == 'yes':
                    probability = random.randint(1, 10)

                    if espada_count > 0:  # Si estás usando una espada
                        if probability <= 4:  # 40% de obtener manzana
                            durabilidad = durabilidad - 1
                            obtener_manzana()  # Replace with actual implementation
                            addText(f'Obtuviste una manzana')
                        elif probability <= 5:  # 10% de obtener espada de madera
                            durabilidad = durabilidad - 1
                            herramienta = random.choice([obtener_escudomadera, obtener_espadamadera])()
                            addText(f'Obtuviste una {herramienta}')
                        else:
                            durabilidad = durabilidad - 1
                            addText('No obtuviste nada')
                    else:  # Si no estás usando una espada
                        if probability <= 4:  # 40% de obtener manzana
                            obtener_manzana()  # Replace with actual implementation
                            addText("Obtuviste una manzana")
                        elif probability <= 6:  # 20% de obtener espada de madera
                            obtener_espadamadera()
                            addText('Obtuviste una espada de madera')
                        else:
                            addText('No obtuviste nada')

                    # Verificar si el árbol debe ser cortado y reiniciar el contador de turnos
                    if durabilidad == 0:
                        talado = True
                        map[row][column] = 't'  # 't' representa un árbol cortado
                        turnos = 0  # Reiniciar el contador de turnos cuando el árbol es cortado
                        addText('¡Has cortado el árbol! Volverá a crecer en 10 turnos.')

                turnos += 1  # Incrementar el contador de turnos después de golpear el árbol

                if talado and turnos >= 10:
                    map[row][column] = 'T'  
                    talado = False
                    turnos = 0
                    addText('¡El árbol ha vuelto a crecer!')
                
            

def attack_enemy(map, position):
    global sword_usos  # Número máximo de usos de la espada
    global lives_character

    for i in range(-1, 2):
        for j in range(-1, 2):
            row = position[0] + i
            column = position[1] + j
            if 0 <= row < len(map) and 0 <= column < len(map[0]) and map[row][column] == 'E2':
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
        map[new_row][new_column] = 'E2'
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

    santuario_position = check_nearby_element(map, character_position, 'S2?')
    if santuario_position:
        # Incrementar la vida
        lives_character += 1
        # Actualizar el mapa
        map[santuario_position[0]][santuario_position[1]] = 'S2 '
        # Mensaje
        addText(f"Has encontrado un santuario, tu vida ha aumentado. Ahora tienes {lives_character} vidas.")

def interactuar_santuario1(map, character_position):
    global lives_character  # Declarar vida_personaje como global

    santuario_position = check_nearby_element(map, character_position, 'S3?')
    if santuario_position:
        # Incrementar la vida
        lives_character += 1
        # Actualizar el mapa
        map[santuario_position[0]][santuario_position[1]] = 'S3 '
        # Mensaje
        addText(f"Has encontrado un santuario, tu vida ha aumentado. Ahora tienes {lives_character} vidas.")

def show_map(map_zelda):
    clearScreen()
    print(map_zelda)

foxlist = [" ", "F"]
fox_spawn = random.choice(foxlist)



def vida_total():
    cursor.execute("""
        SELECT hearts_remaining FROM game
        where game_id = (SELECT MAX(game_id) FROM game);
    """)
    corazones = cursor.fetchone()
    if corazones:
        return corazones[0]
    else:
        return 0

def vida():
    cursor.execute("""
        SELECT hearts_remaining FROM game
        where game_id = (SELECT MAX(game_id) FROM game);
    """)
    corazones = cursor.fetchone()
    if corazones:
        return corazones[0]
    else:
        return 0

def armas():
    try:
        cursor.execute("""
        SELECT COUNT(weapon_name) AS total_quantity
    FROM game_weapons; 
        """)
        contar = cursor.fetchone()
        if contar:
            return contar[0]
        else:
            return 0
    except Exception as e:
        print(f"error in comida {e}")
        return None
def blood_moon():
    cursor.execute("""
        SELECT blood_moon_countdown FROM game
                   WHERE game_id = (SELECT MAX(game_id) FROM game); ;
    """)
    lunaroja = cursor.fetchone()
    if lunaroja:
        return lunaroja[0]
    else:
        return 0
def contar_comida():
    try:
        cursor.execute("""SELECT SUM(quantity_remaining) AS total_quantity
        FROM game_food """)
        comida = cursor.fetchone()
        if comida:
            return comida[0]
        else:
            return 0
    except Exception as e:
        print(f"error in comida {e}")
        return None


def espada():
    try:
        cursor.execute("""
        SELECT quantity_remaining FROM game_weapons
        WHERE weapon_name = 'Sword' and game_id = (SELECT MAX(game_id) FROM game);
        """)
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error in espada: {e}")
        return None



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
def escudo():
    try:
        cursor.execute("""
        SELECT quantity_remaining FROM game_weapons
        WHERE weapon_name = 'Shield' and game_id = (SELECT MAX(game_id) FROM game);
        """)
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error in espada: {e}")
        return None


if fox_spawn == 'F':
    addText("You see a Fox!")
else:
    addText("All the foxes are hidden")

map =   [['*', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',],
            ['*', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', f'{fox_spawn}', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*',' ',f'{get_name()}',' ',' ',' ',' ','♥', f'{vida()}','/', f'{vida_total()} ',' ',' ','*',' ','',''],
            ['*', '~', '~', ' ', ' ', ' ', 'S2?', '', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E2', '', ' ', ' ', ' ', ' ', '*',' ','Blood', 'Moon',' In',' ','', f'{blood_moon()} ',' ','*','',' ',' ','',],                 
            ['*', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E2', '', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*',' ','Equipment',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',''],                
            ['*', 'O', '~', '~', '~', '~', '~', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', 'O', 'O', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*',' ',' ','Sword',' ','','', f'{espada()} ',' ',' ',' ',' ',' ',' ',' ',' ','*'],                
            ['*', '~', '~', '~', '~', '~', '~', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*',' ',' ','Shield','','',' ', f'{escudo()} ',' ',' ',' ',' ',' ',' ',' ','','*'],
            ['*', ' ', ' ', ' ', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],                
            ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
            ['*', 'X', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S3?', '', '', ' ', ' ', ' ', ' ', ' ', '*', ' ',' ','','Food', ' ',f'{contar_comida()}','',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
            ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*','  ','Weapons', '',f'{armas()}',' ',' ',' ',' ',' ',' ',' ',' ','*']
]


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

def actualizar_zona(zona):
    cursor.execute(f"""
        UPDATE game
        SET region_char = '{zona}'
        WHERE game_id = (SELECT MAX(game_id));""")

def movimiento(map, position, direction, steps):
    for _ in range(steps):
        success = move_character(map, position, direction.lower())
        if not success:
            break
        position = find_link(map, 'X')
    return position

while True:
    clearScreen()
    print("* Death Mountain* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print_map(map)
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    showPrompt()
    user_input = input("\nMove to?(direction(wasd) number): ")
    if user_input.lower() == "hyrule":
        addText("You travel to Hyrule")
        actualizar_zona(user_input)
        conexion.commit()
        import hyrule
    if user_input.lower() == "show map":
        addText("Showing Map")
        print(map)
    if user_input.lower() == "necluda":
        addText("You travel to Necluda")
        actualizar_zona(user_input)
        conexion.commit()
        import necluda

    if user_input.lower() == "castle":
        addText("You travel to Castle")
        actualizar_zona(user_input)
        conexion.commit()
        import castle
    if user_input.lower() == "eat vegetables":
        subir_vida("Apple")
    elif user_input.lower() == "eat salad":
            subir_vida("Salad")
    elif user_input.lower() == "eat pescatarian":
            subir_vida("pescatarian")
    elif user_input.lower() == "eat roasted":
            subir_vida("roasted")
    if user_input.lower() == "attack":
        swing_sword()
    user_input = user_input.split()

    if user_input[0].lower() == 'show':
        addText(user_input[0])
        while True:
            show_map(map_zelda)
            showPrompt()
            back = input("Write 'back' if you wanna go back: ")
            if back.lower() == "back":
                addText(back)
                break  
            else:
                addText("Unvalid entry. Try it again.")

    if user_input[0].lower() == 'exit':
        break

    if user_input[0].lower() in ['w', 'a', 's', 'd'] and len(user_input) == 2:
        direction = user_input[0].lower()
        steps = int(user_input[1])
        character_position = movimiento(map, character_position, direction, steps)
        if direction == "w":
            addText(f"Te has movido hacia arriba {steps} casillas.")
            special_symbols(map, character_position)
            if talado == True:
                turnos = turnos + 1
                addText(f"llevas {turnos}")
        elif direction == "a":
            addText(f"Te has movido hacia la izquierda {steps} casillas.")
            special_symbols(map, character_position)
            if talado == True:
                turnos = turnos + 1 
                addText(f"llevas {turnos}")

        elif direction == "s":
            addText(f"Te has movido hacia abajo {steps} casillas.")
            special_symbols(map, character_position)
            if talado == True:
                turnos = turnos + 1
                addText(f"llevas {turnos}")

        elif direction == "d":
            addText(f"Te has movido hacia la derecha {steps} casillas.")
            if talado == True:
                turnos = turnos + 1
                addText(f"llevas {turnos}")
           


    else:
        addText("Entrada no válida. Intenta de nuevo.")
conexion.close()
print("Juego terminado.")
