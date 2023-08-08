from oop.all_exams.exam_retake_22_august_2020.structure_and_func.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        room_total_price = sum([room.room_cost for room in self.rooms])
        room_total_expenses = sum([room.expenses for room in self.rooms])
        return f"Monthly consumption: {room_total_expenses + room_total_price:.2f}$."

    def pay(self):
        return_result = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost

            # Apparently room is family for this loop
            if room.budget >= total_cost:
                room.budget -= total_cost
                return_result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                return_result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return '\n'.join(return_result)

    # Absurd to make it look good
    def status(self):
        result = []
        total_population = 0
        for room in self.rooms:
            total_population += room.members_count
            current_text = [f"{room.family_name} with {room.members_count} members."
                            f" Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"]

            counter = 0
            for child in room.children:
                counter += 1
                current_text.append(
                    f"--- Child {counter} monthly cost: {child.get_monthly_expense():.2f}$")

            current_text.append(f"--- Appliances monthly cost:"
                                f" {sum([x.get_monthly_expense() for x in room.appliances]):.2f}$")
            result.append("\n".join(current_text))
        return f"Total population: {total_population}\n" + "\n".join(result)
