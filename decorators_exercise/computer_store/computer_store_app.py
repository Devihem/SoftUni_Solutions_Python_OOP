from decorators_exercise.computer_store.computer_types.desktop_computer import DesktopComputer
from decorators_exercise.computer_store.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTERS = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse = []  # Computers Obj List
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTERS.keys():
            raise ValueError(f"{type_computer} is not a valid type computer!")

        self.warehouse.append(self.VALID_COMPUTERS[type_computer](manufacturer, model))
        return self.warehouse[-1].configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for device in self.warehouse:
            if device.price <= client_budget and device.processor == wanted_processor and device.ram >= wanted_ram:
                self.profits += client_budget - device.price
                self.warehouse.remove(device)
                return f"{device} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")

#  I made some changes without testing them ( to annoying to pack them again , msg me if there is some issue )
