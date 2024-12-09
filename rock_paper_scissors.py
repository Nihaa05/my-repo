import random

def play():
    user = input("what is your choise? 'r' for rock,'p' for paper, 's' for Scissors\n ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s s tie'
    
    # r>s, s>p, p>r
    if is_win(user,computer):
        return 'You won!'
    
    return 'You lost'

def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
    or (player == 'p' and opponent == 'r'):
        return True
    
print(play())