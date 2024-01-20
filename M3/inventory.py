import mysql.connector

conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')

cursor = conexion.cursor()

def armas_db(weapon):
    cursor.execute(f"SELECT quantity_remaining, equiped, lives_remaining FROM game_weapons WHERE weapon_name='{weapon}'")
    armas = cursor.fetchone()
    return armas

def equipped(weapon):
    armas = armas_db(weapon)[1]
    if armas == 1:
        return "(equipped)"
    elif armas == 0:
        return "        "

def quantity(weapon):
    armas = armas_db(weapon)
    return armas[0] if armas else None

def durability(weapon):
    armas = armas_db(weapon)
    return armas[2] if armas else None

print(f"""
* * * * * * Weapons *
*                   *                  
*                   *
* Wood Sword    {durability("Wood Sword")}/{quantity("Wood Sword")} *
*  {equipped("Wood Sword")}         *
* Sword         {durability("Sword")}/{quantity("Sword")} *
*  {equipped("Sword")}         *
* Wood Shield   {durability("Wood Shield")}/{quantity("Wood Shield")} *
*  {equipped("Wood Shield")}         *
* Shield        {durability("Shield")}/{quantity("Shield")} *
*  {equipped("Shield")}       *
* * * * * * * * * * *
""")
