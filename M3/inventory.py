import mysql.connector

conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')
cursor = conexion.cursor()


max_hearts = 3

def vida():
    cursor.execute("""
        SELECT hearts_remaining FROM game
    """)
    corazones = cursor.fetchone()
    if corazones:
        return corazones[0]
    else:
        return 0
def vegetables():
    cursor.execute("""
        SELECT quantity_remaining FROM game_food
        WHERE game_id = 1 AND food_name = 'Apple'
        LIMIT 1
    """)
    vegetal = cursor.fetchone()
    if vegetal:
        return vegetal[0]
    else:
        return 0

def pescao():
    cursor.execute("""
        SELECT quantity_remaining FROM game_food
        WHERE game_id = 1 AND food_name = 'Pescao'
        LIMIT 1
    """)
    vegetal = cursor.fetchone()
    if vegetal:
        return vegetal[0]
    else:
        return 0

def zorrito():
    cursor.execute("""
        SELECT quantity_remaining FROM game_food
        WHERE game_id = 1 AND food_name = 'Meat'
        LIMIT 1
    """)
    vegetal = cursor.fetchone()
    if vegetal:
        return vegetal[0]
    else:
        return 0



def total_comida():
    cursor.execute("""SELECT SUM(quantity_remaining) AS total_quantity
FROM game_food;""")
    comida = cursor.fetchone()
    if comida:
        return comida[0]
    else:
        return 0
def contar_armas():
    cursor.execute("""
    SELECT COUNT(weapon_name) AS total_quantity
FROM game_weapons; 
    """)
    contar = cursor.fetchone()
    if contar:
        return contar[0]
    else:
        return 0
def menu(opcio):
    if opcio == "Show inventory main":
        print(inventory)

inventory = (f"""
* * * * * Inventory * * * * * * Weapons * * * * * *  Food *
*                   *                   *                 *
* Link        ♥ {vida()}/{max_hearts} *                   *                 *
*                   * Wood Sword    5/2 * Vegetables {vegetables()}    *
* Equipment         *  (equiped)        * Fish {pescao()}          *
*        Wood Sword * Sword         9/1 * Meat {zorrito()}          *
*            Shield *                   *                 *
*                   * Wood Shield   5/0 * Salads          *
* Food         {total_comida()}   *                   * Pescatarian     *
* Weapons      {contar_armas()}    * Shield        9/2 * Roasted         *
*                   *  (equiped)        *                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")





#opcio = input("What do you want to do?")
#menu(opcio)
print(inventory)
conexion.close()
