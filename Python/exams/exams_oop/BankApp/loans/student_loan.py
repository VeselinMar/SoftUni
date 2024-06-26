from BankApp.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST_RATE_INCREMENTATION = 0.2
    INTEREST_RATE = 1.5
    AMOUNT = 2000.0

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INTEREST_RATE_INCREMENTATION
