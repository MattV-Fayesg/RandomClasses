class Lift:

    def __init__(self):
        self.__floor_limit = 0
        self.__capacity = 0
        self.__person = 0
        self.__floor = 0

    @property
    def person(self):
        return self.__person

    @property
    def floor_limit(self):
        return self.__floor_limit

    @property
    def floor(self):
        return self.__floor

    @property
    def capacity(self):
        return self.__capacity

    @person.setter
    def person(self, person):
        if 0 < person < self.capacity:
            self.__person = person
        else:
            self.__person = 0

    @floor_limit.setter
    def floor_limit(self, floors):
        self.__floor_limit = floors

    @floor.setter
    def floor(self, floor):
        self.__floor = floor

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    def start(self, capacity, floors):
        self.capacity = capacity
        self.floor_limit = floors

    def enter(self):
        if self.capacity > self.person >= 0:
            self.person += 1
        elif self.person > self.capacity:
            return f"Lift doesn't support {self.person + 1} persons"
        else:
            return f'This lift is empty!'

    def exit(self):
        if self.person > 0:
            self.person -= 1
        else:
            return f'This lift is empty!'

    def up(self):
        if self.floor_limit > self.floor >= 0:
            self.floor += 1
        elif self.floor >= self.floor_limit:
            return f"This lift doesn't go that high!"
        else:
            return f"This lift doesn't go that low"

    def down(self):
        if self.floor > 0:
            self.floor -= 1
        else:
            return f"This lift doesn't go that low"


# # Running it
# elevator = Lift()
# elevator.start(10, 5)
# print(f'{elevator.floor} floor')
# print(f'{elevator.person} persons')
# elevator.up()
# print(f'{elevator.floor} floor')
# print(f'{elevator.person} persons')
# elevator.enter()
# elevator.up()
# print(f'{elevator.floor} floor')
# print(f'{elevator.person} persons')
# elevator.exit()
# print(f'{elevator.floor} floor')
# print(f'{elevator.person} persons')
# elevator.up()
# elevator.up()
# print(f'{elevator.floor} floor')
# print(f'{elevator.person} persons')
# elevator.up()
# print(f'{elevator.floor} floor')
# print(f'{elevator.person} persons')
# print(elevator.up())  # Hit the limit
# elevator.down()
# elevator.down()
# elevator.down()
# elevator.down()
# elevator.down()
# print(f'{elevator.floor} floor')
# print(f'{elevator.person} persons')
# print(elevator.down())  # Hit the limit
