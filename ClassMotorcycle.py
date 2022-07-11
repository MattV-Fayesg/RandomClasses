class Motorcycle:

    def __init__(self, brand, motorcycle_model, color, gear=0, max_gear=2, min_gear=0, power=False):
        self.__power = power
        self.__brand = brand
        self.__motorcycle_model = motorcycle_model
        self.__color = color
        self.__gear = gear
        self.__max_gear = max_gear
        self.__min_gear = min_gear

    @property
    def power(self):
        if self.__power:
            return "On"
        else:
            return "Off"

    @property
    def brand(self):
        return self.__brand

    @property
    def motorcycle_model(self):
        return self.__motorcycle_model

    @property
    def color(self):
        return self.__color

    @property
    def gear(self):
        return self.__gear

    @property
    def max(self):
        return self.__max_gear

    @property
    def min(self):
        return self.__min_gear

    @gear.setter
    def gear(self, gear):
        self.__gear = gear

    @power.setter
    def power(self, onoff):
        self.__power = onoff

    def gear_up(self):
        if self.max > self.gear >= self.min:
            self.gear += 1
        else:
            return 'This motorcycle has only 2 gears + neutral'

    def gear_down(self):
        if self.max >= self.gear > self.min:
            self.gear -= 1
        else:
            return f'This motorcycle has only {self.max} gears + neutral'

    def power_on(self):
        if not self.__power:
            self.__power = True
        else:
            return f"Power is already on"

    def power_off(self):
        if self.__power:
            self.__power = False
        else:
            return f"Power is already off"

    def show_bike(self):
        return f'Motorcycle info:\n' \
               f' On/Off: {self.power}\n' \
               f' brand: {self.brand}\n' \
               f' model: {self.motorcycle_model}\n' \
               f' color: {self.color}\n' \
               f' which gear its on {self.gear} gear\n' \
               f' Max gear available: {self.max} ' \
               f'|Min gear available: {self.min}\n' \
               f'---------------------------------'


bike = Motorcycle('Gold Wing Tour', 'Honda', 'black')
print(bike.show_bike())
bike.gear_up()
print(bike.show_bike())
bike.gear_up()
print(bike.show_bike())
bike.gear_up()
print(bike.show_bike())
bike.gear_down()
print(bike.show_bike())
bike.gear_down()
print(bike.show_bike())
bike.power_on()
print(bike.show_bike())
bike.power_off()
print(bike.show_bike())
