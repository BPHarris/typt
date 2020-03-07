from money import Money
from decimal import Decimal


def main():
    user_balance = Money(0.0, 'GBP')

    # Example 1: Adding integer
    print('Your balance + £10:', user_balance.amount + 10)

    # Example 2: Adding float
    print('Your balance + £3.75:', user_balance.amount + 3.75)


if __name__ == '__main__':
    main()
