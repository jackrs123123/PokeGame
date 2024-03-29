'''
Same program given new tools to work with (dicts, move functions, and the start of a mediocre gui) (3/27/24)
    - things to add: full attack pallet functionality for each player with different outcomes responding to each
'''

import random
import time

user_hp = 100
enemy_hp = 100 # both are accessed when player loop is first called

user_attacks = { # attack:[damage, pp]
                'CONFUSE RAY':[None, 10], 
                'NIGHT SHADE':[25, 15],
                'HYPNOSIS':[None, 20],
                'DREAM EATER':[None, 15]
               }

enemy_attacks = { # attack:[damage, pp]
                 'PSYCHIC':[35, 10],
                 'RECOVER':[None, 10]
                }

def night_shade(hp): # user move
    hp -= user_attacks['NIGHT SHADE'][0]
    return hp

def psychic(hp): # enemy move
    hp -= enemy_attacks['PSYCHIC'][0]
    return hp

def t1():
    time.sleep(1)

def user_choice_loop(u, e): # allows player to make choices throughout duration of game
    
    t1()
    print(list(user_attacks.keys()))

    u_inp = input()

    if u_inp == 'n':
        e = night_shade(e)
        t1()
        print('you did', user_attacks['NIGHT SHADE'][0], 'damage with', list(user_attacks.keys())[1])
    else:
        t1()
        print('move not yet coded in!')
    
    if e > 0:
        enemy_choice_loop(u, e)
    else:
        t1()
        print('Enemy died!')
        t1()
        print('You have won the battle!')

def enemy_choice_loop(u, e): # called by user loop to repeat turn sequence

    en_inp = random.choice(list(enemy_attacks.keys()))

    if en_inp == 'PSYCHIC':
        u = psychic(u)
        t1()
        print('enemy did', enemy_attacks['PSYCHIC'][0], 'damage with', list(enemy_attacks.keys())[0])
    else:
        t1()
        print('enemy attack is null (unfinished code here)')

    t1()
    print('You:', u, 'Enemy:', e)

    if u > 0:
        user_choice_loop(u, e)
    else:
        t1()
        print('You died!')
        t1()
        print('You have lost the battle!') 

print('You:', user_hp, 'Enemy:', enemy_hp)
user_choice_loop(user_hp, enemy_hp)