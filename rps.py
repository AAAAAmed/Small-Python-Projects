import random

win=False
while True:
    player=input('Type "r" "p" or "s" ')
    if player=='r' or player=='p' or player=='s':
        cpu=random.randint(0, 2)
        if player=='r':
            player=0
        elif player=='p':
            player=1
        else:
            player=2

        if player==0 and cpu==2:
            win==True
        elif player==2 and cpu==0:
            win==False
        elif player==cpu:
            win==0
        elif player>cpu:
            win=True
        
        if player==0:
            player='rock'
        elif player==1:
            player='paper'
        else:
            player='scissors'
        
        if cpu==0:
            cpu='rock'
        elif cpu==1:
            cpu='paper'
        else:
            cpu='scissors'
    
        print(f'You played {player}.')
        print(f'CPU played {cpu}.')

        if win:
            print('You won!')
        elif win==0:
            print("It's a draw.")
        else:
            print('You lost :(')
        
    elif player.lower()=='exit':
        break
    else:
        print('This is not a valid input, please try again.')
        continue