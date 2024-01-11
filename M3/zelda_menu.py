from ascii import menu
from ascii import help_mainmenu
from ascii import saved_games
from ascii import help_saves_games
from ascii import new_game
from ascii import help_new_game
from ascii import about
from ascii import legend
from ascii import plot

savedGames = []

def player():

    return

#def confirm_name(name):
    if (name.len() >= 3) and (name.len() <= 10):
        for letter in name:
            if not 

    return








def mainmenu():
    sortir = True
    while sortir == True:
        print(menu)
        option = input("What to do now? ")
        option = option.lower()
        while True: 
            if option == "exit":
                sortir = False
                break

            if option == "new game":
                print(new_game)
                option_newgame = input("What to do now ? ")
 
                if option_newgame == "Back":
                    break
                elif option_newgame == "Help":
                    print(help_new_game)
                    option_newgame = input("What to do now ? ")
                    if option_newgame == "Back":
                        option = "new game"
                elif option_newgame <= 10 and option_newgame >= 3:
                    savedGames.append(option_newgame)
                    print(savedGames)
 

            if option == "help":
                print(help_mainmenu)
                optionhelp = input("What to do now ? ")
                if optionhelp == "Back":
                    break
                else:
                    return "Incorrect option"
            
            elif option == "about":
                print(about)
                option_about = input("What to do now ? ")
                if option_about == "Back":
                    break
                else:
                    return "Incorect option"

            elif option == "continue":
                print("Continue")
        


mainmenu()








