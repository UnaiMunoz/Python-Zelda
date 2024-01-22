import mysql.connector

conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')

cursor = conexion.cursor()


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

#MENU ARMAS FUNCIONES
def durability(arma):
    cursor.execute(f"""
        SELECT lives_remaining FROM game_weapons
        where weapon_name ='{arma}' and game_id = (SELECT MAX(game_id) FROM game);
    """)
    usos = cursor.fetchone()
    if usos:
        return usos[0]
    else:
        return 0
def equipado(arma):
    cursor.execute(f"""
        SELECT equiped FROM game_weapons
        WHERE weapon_name = '{arma}' AND game_id = (SELECT MAX(game_id) FROM game);
    """)
    equipo = cursor.fetchone()
    if equipo:
        return equipo[0]
    else:
        return 0
    

def cantidad(arma):
    cursor.execute(f"""
        SELECT quantity_remaining FROM game_weapons
        WHERE weapon_name = '{arma}' AND game_id = (SELECT MAX(game_id) FROM game);
    """)
    golpes = cursor.fetchone()
    if golpes:
        return golpes[0]
    else:
        return 0
    

def equip(arma):
    try:
        cursor.execute(f"""
            SELECT equiped FROM game_weapons
            WHERE weapon_name = '{arma}' AND game_id = (SELECT MAX(game_id) FROM game);
        """)
        equipo = cursor.fetchone()
        
        if equipo is not None:
            if equipo[0] == 0:
                return 1
            else:
                return 0                
        else:
            print(f"Weapon {arma} not found in the latest game.")

    
    except Exception as e:
        print(f"Error: {e}")
    
 #FUNCIONES COMIDA
def contar_manzanas():
        cursor.execute(f"""
            SELECT quantity_remaining FROM game_food
            WHERE food_name = 'Apple' AND game_id = (SELECT MAX(game_id) FROM game);
        """)    
        manzana = cursor.fetchone()
        if manzana:
            return manzana[0]
        else:
            return 0

def contar_pescados():
        cursor.execute(f"""
            SELECT quantity_remaining FROM game_food
            WHERE food_name = 'pescao' AND game_id = (SELECT MAX(game_id) FROM game);
        """)    
        manzana = cursor.fetchone()
        if manzana:
            return manzana[0]
        else:
            return 0
def contar_carne():
        cursor.execute(f"""
            SELECT quantity_remaining FROM game_food
            WHERE food_name = 'Meat' AND game_id = (SELECT MAX(game_id) FROM game);
        """)    
        manzana = cursor.fetchone()
        if manzana:
            return manzana[0]
        else:
            return 0
        
def contar_salad():
        cursor.execute(f"""
            SELECT quantity_remaining FROM game_food
            WHERE food_name = 'Salad' AND game_id = (SELECT MAX(game_id) FROM game);
        """)    
        manzana = cursor.fetchone()
        if manzana:
            return manzana[0]
        else:
            return 0
def contar_pescatarian():
        cursor.execute(f"""
            SELECT quantity_remaining FROM game_food
            WHERE food_name = 'pescatarian' AND game_id = (SELECT MAX(game_id) FROM game);
        """)    
        manzana = cursor.fetchone()
        if manzana:
            return manzana[0]
        else:
            return 0
def contar_roasted():
        cursor.execute(f"""
            SELECT quantity_remaining FROM game_food
            WHERE food_name = 'roasted' AND game_id = (SELECT MAX(game_id) FROM game);
        """)    
        manzana = cursor.fetchone()
        if manzana:
            return manzana[0]
        else:
            return 0

print(f"""
* * * * * * Inventory *
*                     *                   
* {get_name()}         ♥{vida()} /{vida_total()} *
*                     *
*Equipment            *
*               Sword *
*              Shield *
*                     *
*                     *
* Food            {contar_comida()}  *
* Weapons         {armas()}   *
* * * * * * * * * * * *
""")
print(f"""
* * * * * *Food * * * *
*                     *                   
*                     *
* Wood Sword     {durability("Wood Sword")}/{cantidad("Wood Sword")}  *
*  Equipped:     {equip("Wood Sword")}    *
* Sword          {durability("Sword")}/{cantidad("Sword")}  *
*  Equipped:     {(equip(("Sword")))}    *
* Wood Shield    {durability("Wood Shield")}/{cantidad("Wood Shield")}  *
*  Equipped:     {(equip(("Wood Shield")))}    *
* Shield         {durability("Shield")}/{cantidad("Shield")}  *
*  Equipped:     {(equip(("Shield")))}    *
* * * * * * * * * * * *
""")
print(f"""
* * * * * *Food * * * *
*                     *                   
*Vegetables {contar_manzanas()}        *
*                     *
*Fish  {contar_pescados()}              *
*Meat  {contar_carne()}              *
*                     *
*Salads {contar_salad()}             *
*Pescatarian {contar_pescatarian()}        *
*Roasted {contar_roasted()}            *
*                     *
* * * * * * * * * * * *
""")

# Close the connection
conexion.close()
