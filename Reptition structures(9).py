TAX_FACTOR= 0.0065

print('Enter the property lot number')
print('or enter 0 to end.')
lot=int(input('Lot number: '))

while lot != 0:
    value=float(input('Enter the property value: '))
    tax=value*TAX_FACTOR
    print('property tax: $', format(tax, ',.2f'), sep='')

    print('enter the next lot number or')
    print('enter 0 to end.')
    lot=int(input('Lot number: '))