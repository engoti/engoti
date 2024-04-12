#use of if statement together with relational operators
HIGH_SCORE=95

test1=int(input('This is test number 1: '))
test2=int(input('This is test number 2: '))
test3=int(input('This is test number 3: '))

average=(test1+test2+test3)/3

print('The average score is',average)

if average>=HIGH_SCORE:
    print('congratulations')
    print('That is a great average')