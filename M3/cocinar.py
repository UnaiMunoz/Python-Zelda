import random
import os
import mysql.connector

conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')

cursor = conexion.cursor()

def cocinar(cooking):
    if cooking.lower() == "salad":
        ensalada = "You selected Salad"
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining - 2
        WHERE food_name = 'Apple' AND quantity_remaining >= 2;""")
        if cursor.rowcount == 0:
            print("You can't cook that! Not enough 'Apple' available.")
        else:
        #AÑADIR ENSALADA
            cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining + 1
            WHERE food_name = 'Salad';""")
        #PESCADO
    elif cooking.lower() == "pescatarian":
        pescadito = "You selected Pescatarian"
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
            print("You need more food!!")

        #ROASTED
    elif cooking.lower() == "roasted":
        pescadito = "You selected roasted"
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
            print("You need more food!!")
    #MEAT
    elif cooking.lower() == "roasted":
        roasted = "You selected Roasted"
        cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining - 1
            WHERE food_name = 'Meat' AND quantity_remaining >= 1;
        """)
        cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining - 1
            WHERE food_name = 'Apple' AND quantity_remaining >= 1;
        """)
        if cursor.rowcount == 0:
            print("You can't cook that! Not enough 'Apple or Meat' available.")
        # AÑADIR ROASTED
        cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining + 1
            WHERE food_name = 'roasted' AND quantity_remaining >= 0;
        """)
    else:
        print("You cant cook that!!!")
cooking = input("What do you wanna cook?(Salad/Pescatarian/Roasted)")
cocinar(cooking)
conexion.commit()
conexion.close()

