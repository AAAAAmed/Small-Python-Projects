x=None
def replace(wrong, correct):
    global x
    x=correct.join(x.split(wrong))

while 1:
    x=input('> ')
    if x=='exit' or x=='quit':
        break

    replace('^', '**')
    replace('x', '*')

    print(eval(x))
