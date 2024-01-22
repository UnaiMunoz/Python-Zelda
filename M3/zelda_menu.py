import random
import os
from ascii import menu
from ascii import help_mainmenu
from ascii import saved_games
from ascii import help_saves_games
from ascii import new_game
from ascii import help_new_game
from ascii import about
from ascii import legend
from ascii import plot
from datetime import date
import mysql.connector

conexion = mysql.connector.connect(user='root', password='david',
                                   host='localhost',
                                   database='Zelda')
cursor = conexion.cursor()
hoy = date.today()
corazones = 3
corazones_max = 3

def clearScreen():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':  # Para sistemas basados en Unix/Linux/Mac
        os.system('clear')
    elif sistema_operativo == 'nt':  # Para sistemas Windows
        os.system('cls')

prompt_historial = []

def addText(texto):
    prompt_historial.append(texto)

    if len(prompt_historial) > 8:
        prompt_historial.pop(0)

def showPrompt():
    if prompt_historial:
        print("Latest actions: ")
        for prompt in prompt_historial:
            print("->" + " " + prompt)
    else:
        print("There are no actions yet")

def dar_id():
    cursor.execute('SELECT MAX(game_id) FROM game')
    ultima = cursor.fetchone()[0]
    nueva_id = ultima + 1
    return nueva_id

def NuevoJugador(Name,id):
    #COMIDA
    cursor.execute(f"INSERT INTO game VALUES ({id}, '{Name}', '{hoy}', {corazones}, 25, 0, 'Hyrule', {corazones_max})")
    cursor.execute(f"INSERT INTO game_food VALUES ({id}, 'Apple', 0)")
    cursor.execute(f"INSERT INTO game_food VALUES ({id},'Meat',0)")
    cursor.execute(f"INSERT INTO game_food VALUES({id},'pescao',0)")
    cursor.execute(f"INSERT INTO game_food VALUES ({id},'pescatarian',0)")
    cursor.execute(f"INSERT INTO game_food VALUES ({id},'roasted',0)")
    cursor.execute(f"INSERT INTO game_food VALUES ({id},'Salad',0)")
    #WEAPONS
    cursor.execute(f"INSERT INTO game_weapons VALUES ({id},'Shield',0,9,0)")
    cursor.execute(f"INSERT INTO game_weapons VALUES ({id},'Sword',0,9,0)")
    cursor.execute(f"INSERT INTO game_weapons VALUES ({id},'Wood Sword',0,5,0)")
    cursor.execute(f"INSERT INTO game_weapons VALUES ({id},'Wood Shield',0,9,0)")
    conexion.commit()
    conexion.close()    

def validateName(name):
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0º23456789 "
    if all(caracter in allowed_characters for caracter in name):
        if (len(name) >= 3) and (len(name) <= 10):
            return True
    else:
        return False    

def mainmenu():
    sortir = True
    while sortir == True:
        clearScreen()
        print(menu)
        showPrompt()
        option = input("\nWhat to do now? ")
        addText(option)
        option = option.lower()
        while True: 
            if option == "exit":
                print("You leave the game")
                sortir = False
                break
 
            while option == "new game":
                clearScreen()
                print(new_game)
                showPrompt()
                option_game = input("\nWhat's your name (Link) ? ")
                while option_game == "Help":
                    addText("Help")
                    clearScreen()
                    print(help_new_game)
                    showPrompt()
                    option_game2 = input("\nWhat to do now ? ")
                    if option_game2 == "Back":
                        addText("Back")
                        break
                    else: 
                        addText("Invalid action")
                while validateName(option_game) == True and option_game != "Back":
                    clearScreen()
                    NuevoJugador(option_game,dar_id())
                    addText(f'Welcome to the game, "{option_game}"')
                    print(legend)
                    showPrompt()
                    option_legend = input("\nType 'continue' to continue ")
                    if option_legend.lower() == "continue":
                        clearScreen()
                        addText(option_legend)
                        print(plot)
                        showPrompt()
                        option_plot = input("\nType 'continue' to continue: ")
                        if option_plot.lower() == "continue":
                            clearScreen()
                            import hyrule   
                    else:
                        addText("Invalid action")

                if option_game == "":
                    option_game = 'link'
                    clearScreen()
                    NuevoJugador(option_game,dar_id())
                    addText(f'Welcome to the game, "{option_game}"')
                    print(legend)
                    showPrompt()
                    option_legend = input("\nType 'continue' to continue ")
                    if option_legend.lower() == "continue":
                        clearScreen()
                        addText(option_legend)
                        print(plot)
                        showPrompt()
                        option_plot = input("\nType 'continue' to continue: ")
                        if option_plot.lower() == "continue":
                            clearScreen()
                            import hyrule   
                    else:
                        addText("Invalid action")                    
                elif option_game.lower() == "back":
                    addText(option_game)
                    break
                else:
                    addText(f'"{option_game}" is not a valid name')

            if option == "help":
                clearScreen()
                print(help_mainmenu)
                showPrompt()
                optionhelp = input("\nWhat to do now ? ")
                if optionhelp.lower() == "back":
                    addText(optionhelp)
                    break
                else:
                    addText("Invalid action")
           
                
            elif option == "about":
                clearScreen()
                print(about)
                showPrompt()
                option_about = input("\nWhat to do now ? ")
                if option_about.lower() == "back":
                    addText(option_about)
                    break
                else:
                    addText("Invalid action")
        
mainmenu()

