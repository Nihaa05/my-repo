import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
  #  print(random_num)

    while guess != random_num:
        guess = int(input(f'guess a number between 1 and {x}: '))

        if guess < random_num:
            print('guess again. Too low.')
        elif guess > random_num:
            print('guess again. Too low')

    print('Congrats! You gusses it right. Its',random_num)
guess(10)