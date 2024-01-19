import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(user='root', password='david', host='localhost', database='Zelda')
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_connection(connection):
    if connection:
        connection.close()

def vida_total(cursor):
    cursor.execute("SELECT max_hearts FROM game")
    corazones_totales = cursor.fetchone()
    return corazones_totales[0] if corazones_totales else 0

def vida(cursor):
    cursor.execute("SELECT hearts_remaining FROM game")
    corazones = cursor.fetchone()
    return corazones[0] if corazones else 0

def equipamiento(cursor):
    cursor.execute("SELECT weapon_name, quantity_remaining, equiped FROM game_weapons")
    armas = cursor.fetchall()
    
    equipamiento_str = "* Equipment         *"
    
    for arma in armas:
        equipado = "(equipped)" if arma[2] else "(unequipped)"
        equipamiento_str += f"\n* {arma[0]:<16} * {arma[1]:<5} {equipado}"
    
    equipamiento_str += "\n*                   *"
    
    return equipamiento_str

def food_info(cursor):
    cursor.execute("SELECT food_name, quantity_remaining FROM game_food WHERE game_id = 1")
    alimentos = cursor.fetchall()
    
    alimentos_str = "* Food              *"
    
    for alimento in alimentos:
        alimentos_str += f"\n* {alimento[0]:<16} * {alimento[1]:<5}"
    
    alimentos_str += "\n*                   *"
    
    return alimentos_str

def weapons_info(cursor):
    cursor.execute("SELECT weapon_name, quantity_remaining FROM game_weapons")
    armas = cursor.fetchall()
    
    armas_str = "* Weapons           *"
    
    for arma in armas:
        armas_str += f"\n* {arma[0]:<16} * {arma[1]:<5}"
    
    armas_str += "\n*                   *"
    
    return armas_str

def mostrar_inventario(cursor):
    inventario = (f"""
* * * * * * * * * * Inventory * * * * * * * * *
*                   *                      *
* Link        ♥ {vida(cursor)}/{vida_total(cursor)} *                   *
{equipamiento(cursor)}
* * * * * * * * * * * * * * * * * * * * * * *
""")
    print(inventario)

def mostrar_weapons(cursor):
    print(weapons_info(cursor))

def mostrar_food(cursor):
    print(food_info(cursor))

def main():
    connection = connect_to_database()
    
    if connection:
        try:
            cursor = connection.cursor()

            opcion = "Show inventory main"
            if opcion == "Show inventory main":
                mostrar_inventario(cursor)

                # Preguntar al usuario si desea ver armas o alimentos
                opcion_detalle = input("Do you want to see weapons or food inventory? (Type 'weapons' or 'food'): ")

                if opcion_detalle.lower() == 'weapons':
                    mostrar_weapons(cursor)
                elif opcion_detalle.lower() == 'food':
                    mostrar_food(cursor)

        finally:
            close_connection(connection)

if __name__ == "__main__":
    main()
#opcio = input("What do you want to do?")
#menu(opcio)
print(inventory)
conexion.close()
