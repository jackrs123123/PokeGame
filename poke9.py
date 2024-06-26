import time, random

user_hp = 100
enemy_hp = 100 # used as parameter in first user_choice function

damage_moves = { # attack:[dam, pp, crit, crit_chance, miss_chance, call_word]
                'PUNCH':[40, 5, 15, (1, 5), (1, 8), 'p'], 
                'KICK':[25, 5, 15, (1, 5), (1, 8), 'k'],
                'FURY':[45, 10, 15, (1, 6), (1, 9), 'FURY']
               }

misc_moves = { # move: [effect, pp, call_word]
                 'RECOVER':[35, 10, 'RECOVER']
             }

help_command = {'help':
                       [
                        'Your objective is to fight the ENEMY and make their health reach zero first.', 
                        'Select moves by typing their beginning letter in your terminal!',
                        'This is the official demo for testing (ver 0.9)',
                        'Best of luck!'
                       ]
               }

def t1():
    time.sleep(1)

def d_move(hp, dam, crit, crit_chance, miss_chance):
    '''
    Use Method:
        - choice functions will state attack used, d_move states if it was a missed or critical hit (along with total_dam for appropriate outcome)
    '''
    miss_chance = random.choice(range(miss_chance[0], miss_chance[1]+1))
    if miss_chance != 1:
        crit_chance = random.choice(range(crit_chance[0], crit_chance[1]+1))
        if crit_chance != 1:
            total_dam = dam
            hp -= total_dam
            t1()
            print(total_dam, 'damage was dealt.')
            return hp
        else:
            total_dam = dam + crit
            hp -= total_dam
            t1()
            print('Critical hit!')
            t1()
            print(total_dam, 'damage was dealt.')
            return hp
    else:
        t1()
        print('It missed!')
        return hp

def m_move(hp, eff):
    bound = 100 - eff
    if hp >= bound:
        dif = 100 - hp
        hp = 100
        t1()
        print('Enemy used RECOVER and gained', dif, 'health back!')
        return hp
    elif hp < bound:
        hp += eff
        t1()
        print('Enemy used RECOVER and gained', eff, 'health back!')
        return hp

def user_choice(): # allows player to make choices throughout duration of game
    
    global user_hp, enemy_hp

    t1()
    print(list(damage_moves.keys())[0:2])

    u_inp = input().lower()

    if u_inp == damage_moves['PUNCH'][5]: # if = p
        if damage_moves['PUNCH'][1] > 0: # if pp > 0
            t1()
            print('you used PUNCH!')
            enemy_hp = d_move(
                    enemy_hp,
                    damage_moves['PUNCH'][0],
                    damage_moves['PUNCH'][2],
                    damage_moves['PUNCH'][3],
                    damage_moves['PUNCH'][4]
                  )
            damage_moves['PUNCH'][1] -= 1
        else:
            t1()
            print('Not enough PP for move!')
    elif u_inp == damage_moves['KICK'][5]: # if = k
        if damage_moves['KICK'][1] > 0:
            t1()
            print('you used KICK!')
            enemy_hp = d_move(
                    enemy_hp,
                    damage_moves['KICK'][0],
                    damage_moves['KICK'][2],
                    damage_moves['KICK'][3],
                    damage_moves['KICK'][4]
                )
            damage_moves['KICK'][1] -= 1
        else:
            t1()
            print('Not enough PP for move!')
    elif u_inp == 'help':
        for i in help_command['help']:
            time.sleep(2)
            print(i)
    else:
        t1()
        print('not valid move!')

def enemy_choice():

    global user_hp, enemy_hp

    en_inp = random.choice([list(damage_moves)[2], list(misc_moves)[0]])

    if en_inp == damage_moves['FURY'][5]: # if = FURY
        if damage_moves['FURY'][1] > 0:
            t1()
            print('Enemy used FURY!')
            user_hp = d_move(
                    user_hp,
                    damage_moves['FURY'][0],
                    damage_moves['FURY'][2],
                    damage_moves['FURY'][3],
                    damage_moves['FURY'][4]
                )
            damage_moves['FURY'][1] -= 1
        else:
            t1()
            print('Enemy move is null!')
    else:
        if misc_moves['RECOVER'][1] > 0:
            if enemy_hp == 100:
                if damage_moves['FURY'][1] > 0:
                    t1()
                    print('Enemy used FURY!')
                    user_hp = d_move(
                                        user_hp,
                                        damage_moves['FURY'][0],
                                        damage_moves['FURY'][2],
                                        damage_moves['FURY'][3],
                                        damage_moves['FURY'][4]
                                    )
                    damage_moves['FURY'][1] -= 1
                else:
                    t1()
                    print('Enemy move is null!')
            else:
                enemy_hp = m_move(
                                  enemy_hp,
                                  misc_moves['RECOVER'][0]
                                 )
                misc_moves['RECOVER'][1] -= 1
        else:
            t1()
            print('Enemy move is null')

Game = True

t1()
print("Hello and welcome to PokeGame!")
t1()
print("Type 'help' if you want instructions!")

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