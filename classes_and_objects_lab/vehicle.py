class Vehicle:
    def __init__(self, mileage: int, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []

    def __getitem__(self, index):
        return self.lis[index]
