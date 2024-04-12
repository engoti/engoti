CONTRIBUTION_RATE=0.05

def main():
    gross_pay=float(input('Enter the gross pay: '))
    bonus=float(input('Enter the amount of bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay: $', format(contrib, ',.2f'),
          sep='')
    
def show_bonus_contrib(bonus):
    contrib=bonus*CONTRIBUTION_RATE
    print('Contribution for bonuses: $',format(contrib, ',.2f'),sep='')

main()
