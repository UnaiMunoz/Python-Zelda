import mysql.connector

conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')

cursor = conexion.cursor()

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
    
    
    
print(f"""
* * * * * * Weapons *
*                   *                   
*                   *
* Wood Sword    {durability("Wood Sword")}/{cantidad("Wood Sword")} *
*  Equipped:    {equip("Wood Sword")}   *
* Sword         {durability("Sword")}/{cantidad("Sword")} *
*  Equipped:    {(equip(("Sword")))}*
* Wood Shield   {durability("Wood Shield")}/{cantidad("Wood Shield")} *
*  Equipped:    {(equip(("Wood Shield")))}*
* Shield        {durability("Shield")}/{cantidad("Shield")} *
*  Equipped:    {(equip(("Shield")))}*
* * * * * * * * * * *
""")

# Close the connection
conexion.close()
