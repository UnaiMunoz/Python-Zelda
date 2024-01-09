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
                break

            elif option == "new game":
                print(new_game)
                option_game = input("What to do now ? ")
                if len(option_game) <= 10 and len(option_game) >= 3:
                    return "name"
            
                elif len(option_game) == 0:
                    return "name == Link"
            
                elif option_game == "Back":
                    break

                elif option_game == "Help":
                    print(help_new_game)
                    option_game_help = input("What to do now ? ")
                    if option_game_help == "Back":
                        break
                    else: 
                        return "Incorrect option"
                else:
                    return "Incorrect option"
                
            
            elif option == "help":
                print(help_mainmenu)
                optionhelp = input("What to do now ? ")
                optionhelpvalid = optionhelp.lower()
                if optionhelpvalid == "back":
                    break
                else:
                    return "Incorrect option"
            
            elif option == "about":
                print("About")

            elif option == "continue":
                print("Continue")
        


mainmenu()