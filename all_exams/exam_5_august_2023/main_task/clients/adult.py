from oop.all_exams.exam_5_august_2023.main_task.clients.base_client import BaseClient


class Adult(BaseClient):
    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 4.0)

    def increase_clients_interest(self):
        self.interest += 2
