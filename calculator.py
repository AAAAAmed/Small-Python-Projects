import math

print('Hi!, welcome to the text based calculator. Type "help" to get a list of commands.')
while True:
    userInput=input('> ')

    if userInput.lower()=='exit':
        break

    if userInput.lower()=='help':
        print(' ')
        print('> ADD    -adds two numbers together')
        print('> SUB    -subtracts two numbers')
        print('> MULT   -multiplies two numbers together')
        print('> DIV    -divides two numbers')
        print('> SQRT   -square-roots a number')
        print(' ')
        print('> exit   -exit calculator')
        print('> help   -prints a list of commands')
        print(' ')

    if userInput.upper()=='ADD':
        print('> First number to add:')
        a=float(input('> '))
        print('> Second number to add:')
        b=float(input('> '))

        print(' ')
        print(f'> {str(a+b)}')
        print(' ')

    if userInput.upper()=='SUB':
        print('> First number to subtract:')
        a=float(input('> '))
        print('> Second number to subtract:')
        b=float(input('> '))

        print(' ')
        print(f'> {str(a-b)}')
        print(' ')
    
    if userInput.upper()=='MULT':
        print('> First number to multiply:')
        a=float(input('> '))
        print('> Second number to multiply:')
        b=float(input('> '))
        
        print(' ')
        print(f'> {str(a*b)}')
        print(' ')

    if userInput.upper()=='DIV':
        print('> First number to divide:')
        a=float(input('> '))
        print('> Second number to divide:')
        b=float(input('> '))

        print(' ')
        print(f'> {str(a/b)}')
        print(' ')
    
    if userInput.upper()=='SQRT':
        print('> Number to square-root:')
        a=float(input('> '))

        print(' ')
        print(f'> {str(math.sqrt(a))}')
        print(' ')
