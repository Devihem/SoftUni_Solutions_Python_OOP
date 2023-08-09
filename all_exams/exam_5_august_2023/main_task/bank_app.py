from all_exams.exam_5_august_2023.main_task.clients.adult import Adult
from all_exams.exam_5_august_2023.main_task.clients.student import Student
from all_exams.exam_5_august_2023.main_task.loans.student_loan import StudentLoan
from all_exams.exam_5_august_2023.main_task.loans.mortgage_loan import MortgageLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        created_loan = self.VALID_LOANS[loan_type]()
        self.loans.append(created_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        created_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(created_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        client_obj = self.searching_for_client_by_id(client_id)
        loan_obj = self.searching_for_loan_by_type(loan_type)

        if (client_obj.__class__.__name__ == "Student" and loan_type != "StudentLoan") \
                or (client_obj.__class__.__name__ == "Adult" and loan_type != "MortgageLoan"):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan_obj)
        client_obj.loans.append(loan_obj)

        return f"Successfully granted {loan_type} to {client_obj.name} with ID {client_obj.client_id}."

    def remove_client(self, client_id: str):
        client_obj = self.searching_for_client_by_id(client_id)
        if not client_obj:
            raise Exception("No such client!")

        if client_obj.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client_obj)
        return f"Successfully removed {client_obj.name} with ID {client_obj.client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                counter += 1

        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1
        return f"Number of clients affected: {counter}."

    def get_statistics(self):

        total_income = []
        total_loans_given = 0
        total_granted_sum = 0
        total_client_interest_rate = 0
        total_loans_sum_not_granted = sum([loan.amount for loan in self.loans])

        for client in self.clients:
            total_income.append(client.income)
            total_loans_given += len(client.loans)
            total_client_interest_rate += client.interest

            for loan in client.loans:
                total_granted_sum += loan.amount

        average_interest_all_clients = 0
        if self.clients:
            average_interest_all_clients = total_client_interest_rate / len(self.clients)

        result = [f"Active Clients: {len(self.clients)}",
                  f"Total Income: {sum(total_income):.2f}",
                  f"Granted Loans: {total_loans_given}, Total Sum: {total_granted_sum:.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {total_loans_sum_not_granted:.2f}",
                  f"Average Client Interest Rate: {average_interest_all_clients:.2f}"]

        return "\n".join(result)

    # HELPERS -------------------------------------------------------------------------------------

    def searching_for_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client

    # Strange?
    def searching_for_loan_by_type(self, loan_type):
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                return loan
