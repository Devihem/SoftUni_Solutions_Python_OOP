from oop.static_and_class_methods_lab.hotel_rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for searched_room in self.rooms:
            if searched_room.number == room_number:
                searched_room.take_room(people)

    def free_room(self, room_number):

        for searched_room in self.rooms:
            if searched_room.number == room_number:
                searched_room.free_room()

    def status(self):
        free_rooms = []
        taken_rooms = []

        for x in self.rooms:
            self.guests += x.guests

            if not x.is_taken:
                free_rooms.append(str(x.number))
            else:
                taken_rooms.append(str(x.number))

        result = [
            f"Hotel {self.name} has {self.guests} total guests",
            f"Free rooms: {', '.join(free_rooms)}",
            f"Taken rooms: {', '.join(taken_rooms)}"
        ]

        return '\n'.join(result)
