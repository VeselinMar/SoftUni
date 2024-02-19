from decimal import Decimal


def calc_simple_interest(principal_amount, interest_rate, time):
    return f'{round((principal_amount * interest_rate) * time, 2)}$'


def calc_compound_interest(principal_amount, interest_rate, times_per_year, time):
    if times_per_year == 0:
        return "Interest has to be paid out at least once a year!"

    rate_decimal = Decimal(interest_rate) / Decimal(times_per_year)
    amount = principal_amount * (1 + rate_decimal) ** (times_per_year * time)
    interest = amount - principal_amount

    return f'{round(interest, 2)}$'


def calc_loan_payment(principal_amount, interest_rate, time):
    r = Decimal(interest_rate) / Decimal(12)
    n = time * 12
    monthly_payment = (principal_amount * r * (1 + r) ** n) / ((1 + r) ** n - 1)

    return f'{round(monthly_payment, 2)}$'


def calculate_future_value(principal_amount, regular_contribution, interest_rate, compounding_frequency, time):
    n = compounding_frequency * time
    rate_decimal = Decimal(interest_rate) / Decimal(compounding_frequency)

    future_value = (regular_contribution * ((1 + rate_decimal) ** n - 1) / rate_decimal +
                    principal_amount * (1 + rate_decimal) ** n)

    return f'{round(future_value, 2)}$'


def main_menu():
    while True:
        valid = ['1', '2', '3', '4', '5']
        print("1. Calculate Simple Interest\n2. Calculate Compound Interest\n"
              "3. Calculate Loan Payment\n4. Calculate Future Value of Savings\n5. Quit the application")

        task = input("What would you like to calculate: (Type 1-5) ")
        if task not in valid:
            print('Please pick a valid option 1-5')
        elif task == '5':
            print('Goodbye')
            break
        elif task == '1':
            print(calc_simple_interest(
                principal_amount=Decimal(input('Principal amount: $')),
                interest_rate=Decimal(input('Interest rate (%): ')) / 100,
                time=int(input('Time (in years): '))
            ))
        elif task == '2':
            print(calc_compound_interest(
                principal_amount=Decimal(input('Principal amount: $')),
                interest_rate=Decimal(input('Interest rate (%): ')) / 100,
                times_per_year=int(input('Compounding frequency per year: ')),
                time=int(input('Time (in years): '))
            ))
        elif task == '3':
            print(calc_loan_payment(
                principal_amount=Decimal(input('Principal amount: $')),
                interest_rate=Decimal(input('Interest rate (%): ')) / 100,
                time=int(input('Time (in years): '))
            ))
        elif task == '4':
            print(calculate_future_value(
                principal_amount=Decimal(input('Initial principal amount: $')),
                regular_contribution=Decimal(input('Regular contribution: $')),
                interest_rate=Decimal(input('Interest rate (%): ')) / 100,
                compounding_frequency=int(input('Compounding frequency per year: ')),
                time=int(input('Time (in years): '))
            ))
        repeat = input("Do you want to perform another calculation? (yes/no) ")
        if repeat.lower() == 'no':
            print('Goodbye')
            break


main_menu()
