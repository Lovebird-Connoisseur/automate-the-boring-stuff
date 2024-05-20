import random

turn = 1
wins = 0
losses = 0
ties = 0
choices = ['top-l', 'top-m', 'top-r', 'mid-l', 'mid-m', 'mid-r', 'bottom-l', 'bottom-m', 'bottom-r']
Board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
         'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
         'bottom-l': ' ', 'bottom-m': ' ', 'bottom-r': ' '}


def print_board(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['bottom-l'] + '|' + board['bottom-m'] + '|' + board['bottom-r'])


for i in range(10):
    if turn == 1:
        while True:
            move = input('Chose your play:')
            if Board[move] != 'o':
                Board[move] = 'x'
                turn = 0
                break
            else:
                print('Invalid command, chose again')
                continue
    else:
        while True:
            move = random.choice(choices)
            if Board[move] != 'x':
                Board[move] = 'o'
                turn = 1
                print_board(Board)
                break
            else:
                continue


if Board['top-l'] == 'x' and Board['top-m'] == 'x' and Board['top-r'] == 'x':
    print("You win!")
    wins += 1
if Board['mid-l'] == 'x' and Board['mid-m'] == 'x' and Board['mid-r'] == 'x':
    print("You win!")
    wins += 1
if Board['bottom-l'] == 'x' and Board['bottom-m'] == 'x' and Board['bottom-r'] == 'x':
    print("You win!")
    wins += 1
if Board['top-l'] == 'x' and Board['mid-l'] == 'x' and Board['bottom-l'] == 'x':
    print("You win!")
    wins += 1
if Board['top-m'] == 'x' and Board['mid-m'] == 'x' and Board['bottom-m'] == 'x':
    print("You win!")
    wins += 1
if Board['top-r'] == 'x' and Board['mid-r'] == 'x' and Board['bottom-r'] == 'x':
    print("You win!")
    wins += 1
if Board['top-l'] == 'x' and Board['mid-m'] == 'x' and Board['bottom-r'] == 'x':
    print("You win!")
    wins += 1
if Board['top-r'] == 'x' and Board['mid-m'] == 'x' and Board['bottom-l'] == 'x':
    print("You win!")
    wins += 1
if Board['top-l'] == 'o' and Board['top-m'] == 'o' and Board['top-r'] == 'o':
    print("You lose!")
    losses += 1
if Board['mid-l'] == 'o' and Board['mid-m'] == 'o' and Board['mid-r'] == 'o':
    print("You lose!")
    losses += 1
if Board['bottom-l'] == 'o' and Board['bottom-m'] == 'o' and Board['bottom-r'] == 'o':
    print("You lose!")
    losses += 1
if Board['top-l'] == 'o' and Board['mid-l'] == 'o' and Board['bottom-l'] == 'o':
    print("You lose!")
    losses += 1
if Board['top-m'] == 'o' and Board['mid-m'] == 'o' and Board['bottom-m'] == 'o':
    print("You lose!")
    losses += 1
if Board['top-r'] == 'o' and Board['mid-r'] == 'o' and Board['bottom-r'] == 'o':
    print("You lose!")
    losses += 1
if Board['top-l'] == 'o' and Board['mid-m'] == 'o' and Board['bottom-r'] == 'o':
    print("You lose!")
    losses += 1
if Board['top-r'] == 'o' and Board['mid-m'] == 'o' and Board['bottom-l'] == 'o':
    print("You lose!")
    losses += 1

# if option is invalid, chose again (bot)
# create tie condition
