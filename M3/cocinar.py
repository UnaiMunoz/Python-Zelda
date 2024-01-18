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
        #AÑADIR ENSALADA
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining + 1
        WHERE food_name = 'Salad';""")
        #PESCADO
    elif cooking.lower() == "pescatarian":
        roasted = "You selected Pescatarian"
        cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining - 1
            WHERE food_name = 'pescao' AND quantity_remaining >= 1;
        """)
        cursor.execute("""
            UPDATE game_food
            SET quantity_remaining = quantity_remaining - 1
            WHERE food_name = 'Apple' AND quantity_remaining >= 1;
        """)
        if cursor.rowcount == 0:
            print("You can't cook that! Not enough 'Fish and Apple' available.")
        #AÑADIR ENSALADA
        cursor.execute("""
        UPDATE game_food
        SET quantity_remaining = quantity_remaining + 1
        WHERE food_name = 'pescatarian';""")
        #ROASTED
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

