from money import Money
from decimal import Decimal


def main():
    user_balance = Money(0.0, 'GBP')

    # Give the user £10 and display balance
    user_balance.amount = user_balance.amount + 10
    print('Your balance:', user_balance.amount)

    # The user cashes a cheque and display new balance
    user_balance.amount = user_balance.amount + 3.75
    print('Cheque cashed, new balance:', user_balance.amount)


if __name__ == '__main__':
    main()
