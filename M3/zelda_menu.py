from ascii import menu
from ascii import help_mainmenu
from ascii import saved_games
from ascii import help_saves_games
from ascii import new_game
from ascii import help_new_game
from ascii import about
from ascii import legend
from ascii import plot


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

            while option == "new game":
                print(new_game)
                option_game = input("What to do now ? ")
                while option_game == "Help":
                    print(help_new_game)
                    option_game = input("What to do now ? ")
                    if option_game == "Back":
                        break
                    else: 
                        return "Incorrect option"
                if len(option_game) <= 10 and len(option_game) >= 3:
                    return "name"
                elif len(option_game) == 0:
                    return "name == Link"
                elif option_game == "Back":
                    break
                else:
                    return "Incorrect option"

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
                    return "Incorect optio"

            elif option == "continue":
                print("Continue")
        


mainmenu()