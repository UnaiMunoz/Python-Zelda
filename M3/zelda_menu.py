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

id = 0
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

def validateName(name):
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    if all(caracter in allowed_characters for caracter in name):
        if (len(name) >= 3) and (len(name) <= 10):
            return True
    else:
        return False    
def update_nombre(name,id):
    actualizar = (f"""
            INSERT INTO game (game_id, user_name, date_started, hearts_remaining, blood_moon_countdown, blood_moon_appearances, region_char)
            VALUES ({id}, '{name}', '{hoy}', {corazones}, 0, 0, 'Hyrule');
        """)
    cursor.execute(actualizar)
    conexion.commit()
    conexion.close()

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
                    update_nombre(option_game,id + 1)
                    addText(f'Welcome to the game, "{option_game}"')
                    print(legend)
                    showPrompt()
                    option_legend = input("\nType 'continue' to continue ")
                    if option_legend == "Continue":
                        clearScreen()
                        addText(option_legend)
                        print(plot)
                        showPrompt()
                        option_plot = input("\nType 'continue' to continue: ")
                        clearScreen()
                        import hyrule                           
                    else:
                        addText("Invalid action")

                if len(option_game) == "":
                    option_game = 'link'
                    addText(f'Welcome to the game, "{option_game}"')

                elif option_game == "Back":
                    addText(option_game)
                    break
                else:
                    addText(f'"{option_game}" is not a valid name')

            if option == "help":
                clearScreen()
                print(help_mainmenu)
                showPrompt()
                optionhelp = input("\nWhat to do now ? ")
                if optionhelp == "Back":
                    addText(optionhelp)
                    break
                else:
                    addText("Invalid action")
           
                
            elif option == "about":
                clearScreen()
                print(about)
                showPrompt()
                option_about = input("\nWhat to do now ? ")
                if option_about == "Back":
                    addText(option_about)
                    break
                else:
                    addText("Invalid action")
        
mainmenu()

