class Appliance:

    def __init__(self, power=False):
        self.__power = power

    @property
    def power(self):
        if self.__power:
            return "On"
        else:
            return "Off"

    @power.setter
    def power(self, onoff):
        self.__power = onoff

    def turn_on(self):
        if self.__power:
            return 'Appliance is already on'
        else:
            self.__power = True
            return 'Turning On Appliance'

    def turn_off(self):
        if not self.__power:
            return 'Appliance has been turned off already'
        else:
            self.__power = False
            return 'Turning Off Appliance'

    def show_appliance(self):
        return f'Appliance Status\n' \
               f' On/Off: {self.power}\n'


# # Running
# jbl = Appliance()
# print(jbl.show_appliance())
# jbl.turn_on()
# print(jbl.show_appliance())
# jbl.turn_off()
# print(jbl.show_appliance())
