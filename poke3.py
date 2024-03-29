'''
Does everything poke2.py does but has boolean conditional to end the game when one player's health is <= 0. (3/26/24) Jack RS
'''

import random
import time

user_hp = 100
enemy_hp = 100 # both are accessed when player loop is first called

def t1(): # easier to type than time.sleep(1) for every print statement
    time.sleep(1)

print('You:', user_hp, 'Enemy:', enemy_hp)
time.sleep(1)
print('Make choice?')

def user_choice_loop(u, e): # allows player to make choices throughout duration of game
        
    u_inp = input()

    if u_inp == 'y':
        e -= 50
        time.sleep(1)
        print('your move did 50 damage!') # FIXME: use math to figure out damage value
    else:
        time.sleep(1)
        print('you did not make move')

    if e > 0:
        enemy_choice_loop(u, e)
    else:
        time.sleep(1)
        print('You:', u, 'Enemy:', e)
        time.sleep(1)
        print('Enemy died!')
        time.sleep(1)
        print('You have won the battle!')

def enemy_choice_loop(u, e):
    
    en_choices = ['y', 'n']
    en_inp = random.choice(en_choices)

    if en_inp == 'y':
        u -= 25
        time.sleep(1)
        print('enemy move did 25 damage!') # FIXME: use dictionary call to find damage?
    else:
        time.sleep(1)
        print('enemy is null')
    
    if u > 0:
        time.sleep(1)
        print('You:', u, 'Enemy:', e)
        time.sleep(1)
        print('Make move?')
        user_choice_loop(u, e)
    else:
        time.sleep(1)
        print('You:', u, 'Enemy:', e)
        time.sleep(1)
        print('You died!')
        time.sleep(1)
        print('You have lost the battle!')

user_choice_loop(user_hp, enemy_hp)