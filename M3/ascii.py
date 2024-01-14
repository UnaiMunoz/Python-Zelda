import random

menu1 = ("""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                             ##              *
*                                                             ##              *
*                                                          ##~~~              *
*                                                         ###~~~O             *
*   Zelda, Breath of the Wild                              ###~~~ \           *
*                                                           |@@@|  \          *
*                                                           |   |   \         *
*                                                           =   ==            *
*                                                      %%%%%%%%%%%%           *  
*                                                   %%%%%%%%%%%%%%%           *
* New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * * * * * *
""")
             
menu2 = ("""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *         
*                                                             &&              *  
*                                                            oo &             *
*                                                    $       -- &##           *
*                                                    $$     <<OO####          *
*   Zelda, Breath of the Wild                         $$  //OOO####           *
*                                                      $$// OO#####           *
*                                                       **   OOO###           *
*                                                        &    @@@@\           *
*                                                             Q  Q            *
*                                                             Q  Q            *
* New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * * * * * *
""")

menu3 = ("""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *         
*                                                            &&               *
*                                                           ####              *
*                                                          " || "             *
*                                                       @@@@@@@@@@@@          *
*   Zelda, Breath of the Wild                          @     ||@@@            *
*                                                            |@@@             *
*                                                           @@@               *  
*                                                         @@@||     @         *
*                                                      @@@@@@@@@@@@@          *
*                                                            ||               *
* New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * * * * * *
""")

menus = [menu1, menu2, menu3]
menu = random.choice(menus)


help_mainmenu = ("""
* Help, main menu * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*        Type 'continue' to continue a saved game                             *
*        Type 'new game' to start a new game                                  *
*        Type 'about' to see information about the game                       *
*        Type 'exit' to exit the game                                         *
*                                                                             *
*                                                                             *
*        Type 'back' now to go back to the 'Main menu'                        *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

saved_games = ("""
* Saved games  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                            *
*                                                                            *
*                                                                            *
*                                                                            *
*                                                                            *
*                                                                            *
*                                                                            *   
*                                                                            *
*                                                                            *
*                                                                            *
* Play X, Erase X, Help, Back  * * * * * * * * * * * * * * * * * * * * * * * * 
""")

help_saves_games = ("""
* Help, saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*        Type 'play X' to continue playing the game 'X'                       *
*        Type 'erase X' to erase the game 'X'                                 *
*        Type 'back' now to go back to the main menu                          *
*                                                                             *
*                                                                             *
*                                                                             *
*        Type 'back' now to go back to 'Saved games'                          *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

new_game = ("""
* New game * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                            *
*                                                                            *
*                                                                            *
*        Set your name ?                                                     *
*                                                                            *
*                                                                            *
*                                                                            *
*        Type 'back' now to go back to the 'Main menu'                       *
*                                                                            *
*                                                                            *
* Back, Help * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")
    
help_new_game = ("""
* Help, new game * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                            *
*                                                                            *
*        When asked, type your name and press enter                          *
*        if 'Link' is fine for you, just press enter                         *
*                                                                            *
*        Name must be between 3 and 10 characters long and only              *
*        letters, numbers and spaces are allowed                             *
*                                                                            *
*        Type 'back' now to go back to 'Set your name'                       *
*                                                                            *
* Back * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

about = ("""   
* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*        Game developed by ‘Team 1, The Whales’ :                             *
*                                                                             *
*                                                                             *
*        David Bargados                                                       *
*        Marc Cachinero                                                       *
*        Unai Muñoz                                                           *
*                                                                             *
*        Type 'Back' now to go back to the 'Main menu'                        *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

legend = ("""
* Legend * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                            *
*   10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah  *
*   tribe. The Sheikah were a tribe of warriors who protected the Triforce,  *
*   a sacred relic that granted wishes.                                      *
*                                                                            *
*   But one day, Ganondorf, an evil sorcerer, stole the Triforce and began   *
*   to rule Hyrule with an iron fist.                                        *
*                                                                            *
*   The princess, with the help of a heroic young man, managed to defeat     *
*   Ganondorf and recover the Triforce.                                      *  
*                                                                            *                                                                     
* Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

plot = ("""
* Plot * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                            *
*                                                                            *
*   Now history is repeating itself, and Princess Zelda has been captured by *
*   Ganon. He has taken over the Guardians and filled Hyrule with monsters.  *
*                                                                            *
*                                                                            *
*   But a young man named 'Link' has just awakened and                       *
*   must reclaim the Guardians to defeat Ganon and save Hyrule.              *
*                                                                            *
*                                                                            *
* Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

game = ("""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * Inventory *
*                                                         *                   *
*                                                         * Link        ♥ 5/5 *
*                                                         * Blood moon in     *
*                                                         *                   *
*                                                         * Equipment         *
*                                                         *        Wood Sword *
*                                                         *            Shield *
*                                                         *                   *
*                                                         * Food              *
*                                                         * Weapons           *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

inventory = ("""
* * * * * Inventory * * * * * * Weapons * * * * * *  Food *
*                   *                   *                 *
* Link        ♥ 5/5 *                   *                 *
*                   * Wood Sword    5/2 * Vegetables      *
* Equipment         *  (equiped)        * Fish            *
*        Wood Sword * Sword         9/1 * Meat            *
*            Shield *                   *                 *
*                   * Wood Shield   5/0 * Salads          *
*            Food   *                   * Pescatarian     *
*        Weapons    * Shield        9/2 * Roasted         *
*                   *  (equiped)        *                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

help_inventory = ("""
* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*        Type 'show inventory main' to show the main inventory                *
*              (main, weapons, Food)                                          *
*        Type 'eat X' to eat X, where X is a Food item                        *
*        Type 'Cook X' to Cook X, where X is a Food item                      *
*        Type 'equip X' to equip X, where X is a weapon                       *
*        Type 'unequip X' to unequip X, where X is a weapon                   *
*        Type 'back' now to go back to the 'Game'                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

map = ("""
* Map * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                         *                   *
*   Hyrule         S0                     Death mountain  *                   *
*                                 S2?                     *                   *
*         S1?                                      S3?    *                   *
*                                                         *                   *
*                            Castle                       *                   *
*                                                         *                   *
*                     S4                              S5  *                   *
*  Gerudo                              S6?       Necluda  *                   *
*                                                         *                   *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

hyrule = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','O','O','O'],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ','~','~','~','~','~','~','~','~','~','~','~','~','~','O','O','~','O','O','O','O','~'],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ','C',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ','~','~','~','~','~','~',' ',' ',' ','~','~','~','~','~','~'],
          [' ', ' ', ' ', ' ', ' ','T',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ','~','~','~'],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','E9',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','S0',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','',' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','T',' ',' ',' ',' ',' ',' ',' ',' ',' ','',''],
          ['','O','O',' ',' ',' ',' ','O','O','O','O','O',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','E1',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','S1',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','T',' ','M',' ',' ',' ','F',' ',' ',' ',' ',' ',' ',' '],
          ['O','O','O','O','O','O','O','O','O','O','O',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','','']
]

death_mountain = ("""
* Death mountain  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* O               OOOO                                   *                    *
* O                OOOO        F                         *                    *
* ~~   S2?          OOOO                           E2    *                    *
* ~~~        E2     OOOO       OOOO                      *                    *
* O~~~~~~~~           OOOO   OO    OOOOOOOO              *                    *
* ~~~~~~~~~            OOOOOO            OOOO            *                    * 
*    ~~~          T        OOOO            OO            *                    *
*                T          OO       M                   *                    *
* X   C          T          OO                  S3?      *                    *
*                                                        *                    *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

gerudo = ("""
* Gerudo  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*OOOOOOOOOOOOOOOO                                  M     *                    *
* OOOOO OOOOO              TTT                           *                    *
*                            TT             S4          O*                    *
* E1          C                                        OO*                    *
*                                                      OO*                    *
*            AAAAAA                  E2                  *                    *
*            AAAAAAAA                                    *                    *
*    T      AAAAAAA                 OOOOO        F     ~~*                    *
* X     M     AAA        OOOOO    OOOOO              ~~~~*                    *
*               OOOOOOOOOOOOOOOOOOOO              ~~~~~~~*                    *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

necluda = ("""
* Necluda * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                     M                                   *                   *
* X       E1                      TT              M       *                   *
*OO                C            TT                   ~~~~~*                   *
*OOOOO                                           ~~~~~~~~~*                   *
*OOOO                                              ~~~~~~~*                   *
*              T                    E2            S5 ~~~~~*                   *
*     F       T9                                ~~~~~~~~~~*                   *
*~~            T6                                  ~~~~~~~*                   *
*~~~~~~~~               M      S6            ~~~~~~~~~~~~~*                   *
*~~~~~~~~~~~~                           ~~~~~~~~~~~~~~~~~~*                   *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

castle = ("""
* Castle  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                          *                  *
*       \ /                             Ganon ♥♥♥♥♥♥♥♥     *                  *
*     -- O --                                              *                  *
*       / \                                                *                  *
*                              |>  v-v-v-v   |>            *                  *
*                      ,   ,  /_\  |     |  /_\            *                  *
*                      |\_/|  | |'''''''''''| |            *                  *
*                      (q p),-| | ||  _  || | |'-._ |\     *                  *
* OT!                X  \_/_(/| |    |#|    | | ) '-//     *                  *
* OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO *                  *
* Back, Go, Attack  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

the_end = ("""
* Zelda saved * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*           Congratulations, Link has saved Princess Zelda.                   *
*           Thanks for playing!                                               *
*                                                                             *
*                                                                             * 
*                                                                             *
*                                                                             * 
* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

link_death = ("""
* Link death  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*           Game Over.                                                        *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")


