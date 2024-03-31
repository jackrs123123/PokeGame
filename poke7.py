#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


'''
Made user_hp and enemy_hp global and fixed recursion issue with final while loop with dad. (3/29/24)
    - make all move functions into one and update dictionaries to supply more parameters with crits, misses, etc.
'''

import random
import time

user_hp = 100
enemy_hp = 100 # both are accessed when player loop is first called

user_moves = { # attack:[effect, pp]
                'PUNCH':[40, 5], 
                'KICK':[25, 5],
               }

enemy_moves = { # attack:[effect, pp]
                 'FURY':[45, 10],
                 'RECOVER':[35, 10]
                }

def punch(hp): # Missed? --> Critical ---> Message
    miss = random.choice(range(1, 6)) # 1/5 chance of missing hit
    if miss != 1:
        crit = random.choice(range(1, 9)) # 1/8 chance of critical hit occuring
        dam = user_moves['PUNCH'][0]
        if crit != 1:
            hp -= dam
            t1()
            print('you did', dam, 'damage with', list(user_moves.keys())[0])
            return hp
        else:
            dam += 15
            hp -= dam # critical hits do 15 extra damage
            t1()
            print('Critical hit!')
            t1()
            print('you did', dam, 'damage with', list(user_moves.keys())[0])
            return hp
    else:
        t1()
        print('You missed!')
        return hp

def kick(hp): # user move
    miss = random.choice(range(1, 6)) # 1/5 chance of missing hit
    if miss != 1:
        crit = random.choice(range(1, 9)) # 1/8 chance of critical hit occuring
        dam = user_moves['KICK'][0]
        if crit != 1:
            hp -= dam
            t1()
            print('you did', dam, 'damage with', list(user_moves.keys())[1])
            return hp
        else:
            dam += 15
            hp -= dam
            t1()
            print('Critical hit!')
            t1()
            print('you did', dam, 'damage with', list(user_moves.keys())[1])
            return hp
    else:
        t1()
        print('You missed!')
        return hp

def fury(hp): # enemy move
    miss = random.choice(range(1, 6))
    if miss != 1:
        crit = random.choice(range(1, 9))
        dam = enemy_moves['FURY'][0]
        if crit != 1:
            hp -= dam
            t1()
            print('Enemy did', dam, 'damage with', list(enemy_moves.keys())[0])
            return hp
        else:
            dam += 15
            t1()
            print('Critical Hit!')
            t1()
            print('Enemy did', dam, 'damage with', list(enemy_moves.keys())[0])
            return hp
    else:
        t1()
        print('Enemy missed!')
        return hp

def recover(hp): # enemy move
    hp += enemy_moves['RECOVER'][0]
    return hp

def t1():
    time.sleep(1)

def user_choice(): # allows player to make choices throughout duration of game
    
    global user_hp, enemy_hp

    t1()
    print(list(user_moves.keys()))

    u_inp = input()

    if u_inp == 'p':
        if user_moves['PUNCH'][1] > 0: # main mechanism for checking pp count
            enemy_hp = punch(enemy_hp)
            user_moves['PUNCH'][1] -= 1
        else:
            print('out of pp for PUNCH!')
    elif u_inp == 'k':
        if user_moves['KICK'][1] > 0: # main mechanism for checking pp count
            enemy_hp = kick(enemy_hp)
            user_moves['KICK'][1] -= 1
        else:
            print('out of pp for KICK!')
    else:
        print('not valid move!')

def enemy_choice(): # called by user loop to repeat turn sequence

    global user_hp, enemy_hp

    en_inp = random.choice(list(enemy_moves.keys()))

    if en_inp == 'FURY':
        if enemy_moves['FURY'][1] > 0:
            user_hp = fury(user_hp)
            enemy_moves['FURY'][1] -= 1
        else:
            t1()
            print('enemy is null')
    elif en_inp == 'RECOVER':
        if enemy_moves['RECOVER'][1] > 0: # FIXME: put cap on 100 for enemy health. recover move increases health beyond 100.
            if enemy_hp == 100:
                if enemy_moves['FURY'][1] > 0:
                    user_hp = fury(user_hp, enemy_moves['FURY'][1])
                    enemy_moves['FURY'][1] -= 1
                    t1()
                    print('enemy did', enemy_moves['FURY'][0], 'damage with', list(enemy_moves.keys())[0])
            elif enemy_hp >= 65:
                dif = 100 - enemy_hp
                enemy_hp = 100
                enemy_moves['RECOVER'][1] -= 1
                t1()
                print('Enemy used', list(enemy_moves.keys())[1], 'and gained', dif, 'health back!')
            else:
                enemy_hp = recover(enemy_hp)
                enemy_moves['RECOVER'][1] -= 1
                t1()
                print('Enemy used', list(enemy_moves.keys())[1], 'and gained', enemy_moves['RECOVER'][0], 'health back!')
        else:
            t1()
            print('enemy is null')

Game = True

while Game:
    t1()
    print('You:', user_hp, 'Enemy:', enemy_hp)
    user_choice()
    if enemy_hp <= 0:
        t1()
        print('You:', user_hp, 'Enemy:', enemy_hp)
        t1()
        print('Enemy died!')
        t1()
        print('You have won the battle!')
        Game = False
    else:
        enemy_choice()
        if user_hp <= 0:
            t1()
            print('You:', user_hp, 'Enemy:', enemy_hp)
            t1()
            print('You died!')
            t1()
            print('You have lost the battle!')
            Game = False