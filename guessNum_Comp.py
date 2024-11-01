#computer make the guess, we have say if its correct
import random
def computer_guess(x):
    low =1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could be high because low = high
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C):')
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print('The computer guessed your number, It is', guess)

computer_guess(50)