import random as rd

def guess(x):
    random_num=rd.randint(1,x)
    guess=0
    while guess!=random_num:
        guess=int(input(f'enter between 1 to {x} : '))
        if guess<random_num:
            print('oops ! the number is less than the exact')
        elif guess>random_num:
            print('oops ! the number is greater than the exact')

    print(f'wow ! congrats, {random_num} is the number behind. ')


def cp_guess(y):
    low=1
    high=y
    feedback=''
    while feedback != 'c':
        if low != high:
            guess=rd.randint(low,high)
        else:
            guess=low
        feedback=input(f'if {guess} too high or too low or correct(h)(l)(c)')
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1

        
    print(f'yeah ! computer guessed correctly as {guess}')

cp_guess(10)                        
