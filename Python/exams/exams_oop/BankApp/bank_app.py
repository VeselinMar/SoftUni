from typing import List

from BankApp.clients.adult import Adult
from BankApp.clients.student import Student
from BankApp.loans.mortgage_loan import MortgageLoan
from BankApp.loans.student_loan import StudentLoan


class BankApp:
    TYPES_OF_LOAN = {
        "MortgageLoan": MortgageLoan,
        "StudentLoan": StudentLoan,
    }

    TYPES_OF_CLIENT = {
        "Adult": Adult,
        "Student": Student,
    }

    VALID_COMBINATIONS = {
        "Adult": "MortgageLoan",
        "Student": "StudentLoan",
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[MortgageLoan | StudentLoan] = []
        self.clients: List[Adult | Student] = []

    def add_loan(self, loan_type: str):
        loan = self.TYPES_OF_LOAN.get(loan_type)
        if loan is None:
            raise Exception("Invalid loan type!")
        loan_instance = loan()
        self.loans.append(loan_instance)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        client = self.TYPES_OF_CLIENT.get(client_type)
        if client is None:
            raise Exception("Invalid client type!")
        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."
        client_instance = client(client_name, client_id, income)
        self.clients.append(client_instance)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        self.loan_eligibility_validation(loan_type, client_id)
        loan = None
        client = None
        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                loan = l
                self.loans.remove(l)
                break
        for c in self.clients:
            if c.client_id == client_id:
                client = c
                break
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = None
        for c in self.clients:
            if c.client_id == client_id:
                client = c
                break
        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loan_class = self.TYPES_OF_LOAN.get(loan_type)

        count = 0
        for loan in self.loans:
            if isinstance(loan, loan_class):
                loan.increase_interest_rate()
                count += 1

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        total_clients_income = sum(c.income for c in self.clients)

        loans_count_granted_to_clients = sum(len(c.loans) for c in self.clients)
        granted_sum = sum(sum(l.amount for l in c.loans) for c in self.clients)

        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum(l.amount for l in self.loans)

        total_interest_rate = sum(c.interest for c in self.clients)
        avg_client_interest_rate = (total_interest_rate / len(self.clients) if self.clients else 0)

        return_string = (f"Active Clients: {len(self.clients)}\n"
                         f"Total Income: {total_clients_income:.2f}\n"
                         f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                         f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
                         f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

        return return_string

    def loan_eligibility_validation(self, loan_type: str, client_id: str):
        client = next((c.__class__.__name__ for c in self.clients if c.client_id == client_id), None)
        if loan_type != self.VALID_COMBINATIONS[client]:
            raise Exception("Inappropriate loan type!")
