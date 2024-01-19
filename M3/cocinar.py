import random
import os
import mysql.connector

conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')

cursor = conexion.cursor()

def cocinar(cooking):
    if cooking == "salad":
        ensalada = "You selected Salad"
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining - 2
        WHERE food_name = 'Apple' AND quantity_remaining >= 2;""")
        if cursor.rowcount == 0:
            print("You can't cook that! Not enough 'Apple' available.")
        #AÑADIR ENSALADA
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining + 1
        WHERE food_name = 'Salad' AND quantity_remaining >= 0;""")
        #PESCADO
    elif cooking == "pescatarian":
        pescadito = "You selected Pescatarian"
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining - 1
        WHERE food_name = 'pescao' AND quantity_remaining >= 1;

        UPDATE game_food
        SET quantity_remaining = quantity_remaining - 1
        WHERE food_name = 'Apple' AND quantity_remaining >= 1;
        """)
        if cursor.rowcount == 0:
            print("You can't cook that! Not enough 'Apple or Fish' available.")
        # AÑADIR PESCATARIAN
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining + 1
        WHERE food_name = 'pescatarian' AND quantity_remaining >= 0;
        """)
    elif cooking == "roasted":
        roasted = "You selected Roasted"
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining - 1
        WHERE food_name = 'Meat' AND quantity_remaining >= 1;

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

conexion.commit()
conexion.close()
cooking = input("What do you wanna cook?(Salad/Pescatarian/Roasted)")
cocinar(cooking)
