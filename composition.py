class Room:
    def describe(self):
        print("This is a room in the house.")


class House:
    def __init__(self):
        self.room = Room()

    def show_room(self):
        self.room.describe()


house = House()
house.show_room()
