import random

win='none'
while True:
    player=input('Type "rock" "paper" or "scissors" ')
    if player=='rock' or player=='paper' or player=='scissors':
        cpu=random.randint(0, 2)
        if cpu==0:
            cpu='rock'
        elif cpu==1:
            cpu='paper'
        else:
            cpu='scissors'
        
        print(f'You played {player}.')
        print(f'CPU played {cpu}.')   

        if player==cpu:
            print("It's a draw.")
        elif player=='rock' and cpu=='paper':
            print('You lost :(')
        elif player=='rock' and cpu=='scissors':
            print('You won!')
        elif player=='paper' and cpu=='rock':
            print('You won!')
        elif player=='paper' and cpu=='scissors':
            print('You lost :(')
        elif player=='scissors' and cpu=='rock':
            print('You lost :(')
        elif player=='scissors' and cpu=='paper':
            print('You won!')
        
    elif player.lower()=='exit':
        break
    else:
        print('That is not a valid input, please try again.')
        continue