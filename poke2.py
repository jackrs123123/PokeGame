'''
Second version of pokemon fight game. Includes an infinite loop for both players to take turns making choices. (3/26/24)
    - issue to fix is implementing an end to the turn loop once a player's health reaches 0 or below.
    - while loops and booleans are unfinished code for writing the methods for ending the loop(s).
'''

import random
import time

user_hp = 100
enemy_hp = 100 # cannot be accessed by functions?

print('You:', user_hp, 'Enemy:', enemy_hp)
time.sleep(1)
print('Make choice?')

def user_choice_loop(u, e): # allows player to make choices throughout duration of game

    Enemy = False
    
    if u > 0:
    
        User = True
    
    while User == True:
        
        u_inp = input()

        if u_inp == 'y':
            e -= 25
            time.sleep(1)
            print('your move did 25 damage!')
            break
        else:
            time.sleep(1)
            print('please make move')

    enemy_choice_loop(u, e)

def enemy_choice_loop(u, e):

    User = False

    if e > 0:
        
        Enemy = True
    
    en_choices = ['y', 'n']
    en_inp = random.choice(en_choices)

    if en_inp == 'y':
        u -= 25
        time.sleep(1)
        print('enemy move did 25 damage!')
    else:
        time.sleep(1)
        print('enemy is null')
    
    time.sleep(1)
    print('You:', u, 'Enemy:', e)
    time.sleep(1)
    print('Make move?')

    user_choice_loop(u, e)

user_choice_loop(user_hp, enemy_hp)