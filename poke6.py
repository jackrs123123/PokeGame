'''
Critical hits and missed hit probabilities are added in the move functions! Outcome is also added to move functions.
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

def user_choice_loop(u, e): # allows player to make choices throughout duration of game
    
    t1()
    print(list(user_moves.keys()))

    u_inp = input()

    if u_inp == 'p':
        if user_moves['PUNCH'][1] > 0: # main mechanism for checking pp count
            e = punch(e)
            user_moves['PUNCH'][1] -= 1
        else:
            print('out of pp for PUNCH!')
    elif u_inp == 'k':
        if user_moves['KICK'][1] > 0: # main mechanism for checking pp count
            e = kick(e)
            user_moves['KICK'][1] -= 1
        else:
            print('out of pp for KICK!')
    else:
        print('not valid move!')
    
    if e > 0:
        enemy_choice_loop(u, e)
    else:
        t1()
        print('Enemy died!')
        t1()
        print('You have won the battle!')

def enemy_choice_loop(u, e): # called by user loop to repeat turn sequence

    en_inp = random.choice(list(enemy_moves.keys()))

    if en_inp == 'FURY':
        if enemy_moves['FURY'][1] > 0:
            u = fury(u)
            enemy_moves['FURY'][1] -= 1
        else:
            t1()
            print('enemy is null')
    elif en_inp == 'RECOVER':
        if enemy_moves['RECOVER'][1] > 0: # FIXME: put cap on 100 for enemy health. recover move increases health beyond 100.
            if e == 100:
                if enemy_moves['FURY'][1] > 0:
                    u = fury(u, enemy_moves['FURY'][1])
                    enemy_moves['FURY'][1] -= 1
                    t1()
                    print('enemy did', enemy_moves['FURY'][0], 'damage with', list(enemy_moves.keys())[0])
            elif e >= 60:
                dif = 100 - e
                e = 100
                enemy_moves['RECOVER'][1] -= 1
                t1()
                print('Enemy used', list(enemy_moves.keys())[1], 'and gained', dif, 'health back!')
            else:
                e = recover(e)
                enemy_moves['RECOVER'][1] -= 1
                t1()
                print('Enemy used', list(enemy_moves.keys())[1], 'and gained', enemy_moves['RECOVER'][0], 'health back!')
        else:
            t1()
            print('enemy is null')

    t1()
    print('You:', u, 'Enemy:', e)

    if u > 0:
        user_choice_loop(u, e)
    else:
        t1()
        print('You died!')
        t1()
        print('You have lost the battle!')

user_choice_loop(user_hp, enemy_hp)