def main():
    simple_interest(Principal=10000,rate=0.01,periods=10)

def simple_interest(principal,rate,periods):
    interest=principal*rate*periods
    print('The simple interest will be $', format(interest, ',.2f'), sep='')
