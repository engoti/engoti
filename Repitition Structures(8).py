#Calculating Fibonacci sequence
MAX=5
total=0.0

print('This program calculates the sum of')
print(MAX, 'numbers you will enter.')

for counter in range(MAX):
    number=int(input('enter a number: '))
    total= total + number

    print('The total is', total)