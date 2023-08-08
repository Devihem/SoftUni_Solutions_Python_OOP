from decorators_exercise.computer_store.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
    MAX_RAM = 64
    PRICE_RAM = 100

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        # Processor Check
        if processor not in self.PROCESSORS.keys():
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        # RamCheck
        ram_check = self.ram_check(ram)
        if not ram_check:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        # Creating Computer
        self.processor = processor
        self.ram = ram
        self.price += self.PROCESSORS[processor] + ram_check * self.PRICE_RAM
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    # Helper
    @classmethod
    def ram_check(cls, ram):
        counter = 0
        while 2 ** counter < cls.MAX_RAM:

            counter += 1
            current_ram_index = 2 ** counter
            if current_ram_index == ram:
                return counter
        return None
