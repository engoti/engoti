#Converting a Math Formula to a programming statement
#P is the present value, or the amount that you need to deposit today.
#F is the future value that you want in the account. (In this case, F is $10,000.)
#r is the annual interest rate.
#n is the number of years that you plan to let the money sit in the account.

future_value=float(input('Enter the desired future value: '))
rate=float(input('Enter the annual interest rate: '))
years=int(input('Enter the number of years money will grow: '))
present_value=future_value/(1.0+rate)**years
print('You will need to deposit this amount: ',present_value)
