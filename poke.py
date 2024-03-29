'''
This is a demo to see if I can write a pokemon style fight script into Python. (3/26/24) Jack RS
    - Includes one run of the fight where both players make a move. Has a timer for print output.
'''

import random
import time

user_hp = 100
enemy_hp = 100

print('You:', user_hp, 'Enemy:', enemy_hp)
print('Make move?')

u_inp = input()

if u_inp == 'y':
    enemy_hp -= 25
    time.sleep(1)
    print('your move did 25 damage!')
else:
    time.sleep(1)
    print('please make move')

en_choices = ['y', 'n']
en_inp = random.choice(en_choices)

if en_inp == 'y':
    user_hp -= 25
    time.sleep(1)
    print('enemy move did 25 damage!')
else:
    time.sleep(1)
    print('enemy is null')

time.sleep(1)
print('You:', user_hp, 'Enemy:', enemy_hp)
time.sleep(1)
print('Make move?')