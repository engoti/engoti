print("\nNormal Pyramid")
for i in range(5):
    x = '*' * (2 * i + 1)
    print(f'{x:^10}')

print("\nInvert Pyramid")
for i in range(5):
    x = '*' * (2 * (5 - i) - 1)
    print(f'{x:^10}')

print("\nLeft Sided Pyramid")
for i in range(5):
    x = '*' * i
    print(f'{x:<10}')

print("\nRight Sided Pyramid")
for i in range(5):
    x = '*' * i
    print(f'{x:>10}')
