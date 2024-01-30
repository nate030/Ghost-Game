#Ghost Game
from random import randint
print('I See My Way Out')
feeling_brave=True
score=0
while feeling_brave:
    ghost_door = randint(1, 5)
    print('Five doors I might See')
    print('My killer behind one.')
    print('Which door do you open?')
    door = input('1, 2, 3, 4, or 5?')
    door_num = int(door)
    if door_num == ghost_door:
        print('DEAD')
        feeling_brave = False
    else:
        print('No ghost! +1xp')
        print('You enter the next room.')
        score = score + 1
print('Run Away!')
print('Game over! You scored', score)