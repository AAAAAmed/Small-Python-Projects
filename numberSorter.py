import random # To shuffle the array
import time # To calculate execution time

while True:
    # Get a shuffled array in whatever length
    length=int(input('Array length?'))
    array=[]
    for i in range(length):
        array.append(i+1)
    random.shuffle(array)
    print('Working on it...')

    # Sort the shuffled array using the Bubble Algorithm (why r we shuffling the array if we're gonna sort it right after lol??)
    st=time.time()
    num1=0
    num2=0
    correct=0
    sorted=False
    while(not sorted):
        for i in range(length-1):
            num1=array[i]
            num2=array[i+1]
            if num1>num2:
                array[i]=num2
                array[i+1]=num1
        
        # Checks if array is sorted
        correct=0
        for i in range(length-1):
            num1=array[i]
            num2=array[i+1]
            if num1<num2:
                correct+=1
        
        if correct==length-1:
            sorted=True
    
    print(array)
    print(time.time()-st)
