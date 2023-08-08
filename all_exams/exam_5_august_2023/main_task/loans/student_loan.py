from oop.all_exams.exam_5_august_2023.main_task.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    def __init__(self):
        super().__init__(1.5, 2000.0)

    def increase_interest_rate(self):
        self.interest_rate += 0.2
