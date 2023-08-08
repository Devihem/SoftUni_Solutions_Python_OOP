from oop.static_and_class_methods_exercise.movie_world.customer import Customer
from oop.static_and_class_methods_exercise.movie_world.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []
        pass

    @staticmethod
    def dvd_capacity():
        dvd_max_capacity = 15
        return dvd_max_capacity

    @staticmethod
    def customer_capacity():
        customer_max_capacity = 10
        return customer_max_capacity

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):

        # no need of error handling for judge
        current_dvd = next(filter(lambda key: key.id == dvd_id, self.dvds))
        current_customer = next(filter(lambda key: key.id == customer_id, self.customers))

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):

        # no need of error handling for judge
        current_dvd = next(filter(lambda key: key.id == dvd_id, self.dvds))
        current_customer = next(filter(lambda key: key.id == customer_id, self.customers))

        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"

        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = [*self.customers, *self.dvds]
        result = [str(print_line) for print_line in result]

        return '\n'.join(result)
