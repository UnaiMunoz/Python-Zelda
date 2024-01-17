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

def total_comida():
    cursor.execute("""SELECT SUM(quantity_remaining) AS total_quantity
FROM game_food;""")
    comida = cursor.fetchone()
    if comida:
        return comida[0]
    else:
        return 0
def menu(opcio):
    if opcio == "Show inventory main":
        print(inventory)

inventory = (f"""
* * * * * Inventory * * * * * * Weapons * * * * * *  Food *
*                   *                   *                 *
* Link        ♥ {vida()}/{max_hearts} *                   *                 *
*                   * Wood Sword    5/2 * Vegetables      *
* Equipment         *  (equiped)        * Fish            *
*        Wood Sword * Sword         9/1 * Meat            *
*            Shield *                   *                 *
*                   * Wood Shield   5/0 * Salads          *
* Food         {total_comida()}   *                   * Pescatarian     *
*        Weapons    * Shield        9/2 * Roasted         *
*                   *  (equiped)        *                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")





#opcio = input("What do you want to do?")
#menu(opcio)
print(inventory)
conexion.close()
