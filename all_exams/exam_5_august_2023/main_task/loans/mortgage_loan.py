from oop.all_exams.exam_5_august_2023.main_task.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    def __init__(self):
        super().__init__(3.5, 50000.0)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
