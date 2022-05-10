import random

game_level = [
    [
    ['paper', 'paper', 'rock', 'rock', 'rock', 'rock', 'rock', 'scissors', 'scissors', 'scissors'],
    ['paper', 'paper', 'paper', 'rock', 'rock', 'scissors', 'scissors', 'scissors', 'scissors', 'scissors'],
    ['paper', 'paper', 'paper', 'paper', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock'],
], #####     End of Easy
[
    ['paper', 'paper', 'paper', 'rock', 'rock', 'rock', 'scissors', 'scissors'],
    ['paper', 'paper', 'rock', 'rock', 'rock', 'scissors', 'scissors', 'scissors'],
    ['paper', 'paper', 'paper', 'scissors', 'scissors', 'scissors', 'rock', 'rock'],
], #####   End of Normal
[
    ['paper', 'rock', 'scissors', 'scissors'],
    ['paper', 'paper', 'rock', 'scissors'],
    ['paper', 'scissors', 'rock', 'rock'],
    ]
]###### End of Hard
#######################################################
list_status = [
        ['paper', 'rock'], ['rock', 'scissors'], ['scissors', 'paper']
]
count_player_1 = 0
count_player_2 = 0
selected = ['paper', 'rock', 'scissors']
print("Start Game")
print('1- Easy')
print('2- Normal')
print('3- Hard')
get_level_zero = int(input('Select Level Game: '))
while True:
    list_winner = [None, None]
    print("1- Paper")
    print('2- Rock')
    print('3- scissors')
    get_player = int(input('Please Select Choice: '))
    player_2 = random.choice(game_level[get_level_zero - 1][get_player - 1])
    print(f'player_1{selected[get_player - 1]}')
    print(f'Player_2{player_2}')
    list_winner[0] = selected[get_player - 1]
    list_winner[1] = player_2
    if selected[get_player - 1] == player_2:
        print('equal select', end='\t')
        print(f'Player_1: {count_player_1} VS Player_2: {count_player_2}')
        continue
    if list_winner in list_status:
        count_player_1 += 1
        print(f'Player_1: {count_player_1} VS Player_2: {count_player_2}')
    else:
        count_player_2 += 1
        print(f'Player_1: {count_player_1} VS Player_2: {count_player_2}')
    if count_player_1 == 3:
        print('WINNER Player1')
        break
    if count_player_2 == 3:
        print('WINNER Player2')
        break
print("Game Over")