from ClassAppliance import Appliance


class microwave(Appliance):

    def __init__(self, power=False, door=False):
        super().__init__(power)
        self.__door = door

    @property
    def door(self):
        if self.__door:
            return "Door Open"
        else:
            return "Door Closed"

    @door.setter
    def door(self, open_closed):
        self.__door = open_closed

    def open_door(self):
        self.door = True
        self.power = False

    def close_door(self):
        self.door = False

    def turn_on(self):
        if self.power == 'On' and self.door == 'Door Closed':
            return 'Microwave is already on'
        elif self.power == 'Off' and self.door == 'Door Closed':
            self.power = True
            return 'Turning On Appliance'

    def turn_off(self):
        if self.power == 'Off':
            return 'Microwave has been turned off already'
        elif self.power == 'Off':
            self.power = False
            return 'Turning Off Microwave'

    def status(self):
        return f'Microwave status|\n' \
               f' On/Off: {self.power}\n' \
               f' Door: {self.door}\n'


# Running
microwave = microwave()
# Testing Turning On/off with door closed
microwave.turn_off()
print(microwave.status())
microwave.turn_on()
print(microwave.status())
microwave.turn_off()
print(microwave.status())
# Testing if Open door cuts power
microwave.turn_on()
print(microwave.status())
microwave.open_door()
print(microwave.status())
# Testing Turning On/off with door opened
microwave.turn_on()
print(microwave.status())
microwave.turn_off()
print(microwave.status())
