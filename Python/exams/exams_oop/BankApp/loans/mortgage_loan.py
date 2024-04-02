from BankApp.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE_INCREMENTATION = 0.5
    INTEREST_RATE = 3.5
    AMOUNT = 50000.0

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INTEREST_RATE_INCREMENTATION
