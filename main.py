import time
import random
import os

menu = ["1) Play",
        "2) Options",
        "3) High Score"]

options = ["1) +"
           "2) -"
           "3) *"
           "4) /"
           ]

points = 000

def play():
    gen_num = random.randint(1, 9)

    hints = [gen_num]
    i = 1

    while i != 4:
        gen_dummy = random.randint(1, 9)

        if gen_dummy in hints:
            continue
        else:
            dummy = gen_dummy
            hints.append(dummy)
            i += 1

    random.shuffle(hints)

    try_guss = 3
    print('\n')
    print('     -------------------------------------------------------------------------')
    print('     |                                                                       |')
    print('     |                          GUSS THE NUMBER                              |')
    print('     |                                                                       |')
    print('     -------------------------------------------------------------------------', '\n')
    print('     ', try_guss, 'Try Left.', "             Total Points : ", points, '\n')
    print('     -------------------------------------------------------------------------')
    print('     Try to Guss Which Number the AI Selected ', gen_num, ': \n')
    print('          1) ', hints[0], '                2) ', hints[1], '\n')
    print('          3) ', hints[2], '                4) ', hints[3], '\n')

    while try_guss > 0:
        try_guss -= 1
        usr_num = input('     ')

        if int(usr_num) == gen_num:
            os.system('cls')
            print('\n')
            print('\n')
            print('\n')
            print('     | - - - - - - - - - - - - - - C O R R E C T - - - - - - - - - - - - - - |\n')
            print('     |- - - - - - - - - - - - -  + 1 0  P O I N T S - - - - - - - - - - - - -|')
            time.sleep(2)
            return 1
        elif try_guss == 0:
            os.system('cls')
            print('\n')
            print('\n')
            print('\n')
            print('     | B E T T E R  L U C K  N E X T  T I M E ')
            print('     -------------------------------------------------------------------------')
            print('     |                                                                       |')
            print("     |                       BETTER LUCK NEXT TIME                           |")
            print('     |                                                                       |')
            print('     -------------------------------------------------------------------------', '\n')
            time.sleep(2)
            return 0

        else:
            os.system('cls')
            print('\n')
            print('     -------------------------------------------------------------------------')
            print('     |                                                                       |')
            print('     |                          GUSS THE NUMBER                              |')
            print('     |                                                                       |')
            print('     -------------------------------------------------------------------------', '\n')
            print('     ', try_guss, 'Try Left.', "             Total Points : ", points, '\n')
            print('     -------------------------------------------------------------------------')
            print('     Try to Guss Which Number the AI Selected ', gen_num, ': \n')
            print('          1) ', hints[0], '                2) ', hints[1], '\n')
            print('          3) ', hints[2], '                4) ', hints[3], '\n')
            print('     -------------------------------------------------------------------------')
            print('     |                      !!! WRONG TRY AGAIN !!!                          |')
            print('     -------------------------------------------------------------------------')
            continue


def print_to_display(prnt_this):
    print('\n')
    for i in prnt_this:
        print('     ', i, '\n')

    print('\n')
    print('     Please select your option by enter the number.')
    user_selection = input('     ')
    return int(user_selection)


if __name__ == '__main__':
    os.system('cls')
    print('\n')
    print('     - - - - - - - T H E  N U M B E R   G U S S I N G  G A M E - - - - - - - -')
    print('     -------------------------------------------------------------------------')
    print('     |                              MENU                                     |')
    print('     -------------------------------------------------------------------------')
    usr_menu_selection = print_to_display(menu)

    if usr_menu_selection == 1:
        print("Let's play ")

        while True:
            os.system('cls')
            des = play()

            if des == 1:
                os.system('cls')
                points += 10
                time.sleep(2)

            elif des == 0:
                points -= 10
                if points < 0:
                    os.system('cls')
                    print('\n')
                    print('\n')
                    print('\n')
                    print('     -------------------------------------------------------------------------')
                    print('     |                                                                       |')
                    print("     |                             GAME OVER                                 |")
                    print('     |                                                                       |')
                    print('     -------------------------------------------------------------------------', '\n')
                    time.sleep(3)
                    os.system('python3 main.py')

                else:
                     print('     You got 10 points Decreased, total points : ', points)

    elif usr_menu_selection == 2:
        os.system('cls')
        print('\n')
        print('     -------------------------------------------------------------------------')
        print('     |                             OPTIONS                                   |')
        print('     -------------------------------------------------------------------------')

        usr_opt_selec = print_to_display(options)

    elif usr_menu_selection == 3:
        print('You selected High Score')

    else:
        print('Ooops Somthing Went Wrong...!')
