#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done'
#is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message
#and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.

#Desired Output:

#Invalid input
#Maximum is 10
#Minimum is 2

min = None
max = None

while True :
    sval = input('Enter Number:')
    if sval == 'done': break
    try :
        fval = int(sval)
    except :
        print('Invalid input')
        continue
    if min is None :
        min = fval
        max = fval
    else :
        if fval > max : max = fval
        if fval < min : min = fval

if min is not None :
    print('Maximum is', max)
    print('Minimum is', min)
