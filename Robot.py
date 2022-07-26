from ClassAppliance import Appliance


class Robot(Appliance):
    def __init__(self, name, power=False, battery=101, skills=None, phrases=None):
        super().__init__(power)
        if skills is None and phrases is None:
            skills = ["Say Robot name", "Charge", "Battery Status", "Learn phrases"]
            phrases = []
        self.__name = name
        self.__battery = battery
        self.__skills = skills
        self.__phrases = phrases

    @property
    def name(self):
        return self.__name

    @property
    def battery(self):
        return self.__battery

    @property
    def skills(self):
        return self.__skills

    @property
    def phrases(self):
        return self.__phrases

    @name.setter
    def name(self, name):
        if self.power == "On":
            self.__name = name

    @phrases.setter
    def phrases(self, *args):
        if self.power == "On":
            self.__phrases.append(phrase for phrase in args)

    def say_robot_name(self):
        if self.power == "On":
            self.__battery -= 1
            return f"Hi, Nice to meet you\nMy name is {self.name}"
        else:
            return "..."

    def charge(self):
        if self.power == "On":
            if self.battery < 101:
                self.__battery = 101
                return f"Gimme a minute to charge...\n DONE"
            else:
                return f"I'm fully charged"
        else:
            return '...'

    def battery_status(self):
        if self.power == "On":
            self.__battery -= 1
            if self.battery <= 25:
                return f"Battery: {self.battery}%\n" \
                       f"I think i might need a little charge"

            elif self.battery < 100:
                return f"Battery: {self.battery}%\n"

            elif self.battery >= 100:
                return f"Battery: {self.battery}%\n" \
                       f"I'm full!"
        else:
            return f"..."

    def learn_phrase(self, phrase):
        while len(self.phrases) < 6 and self.power == "On":
            if phrase not in self.phrases:
                self.phrases.append(phrase)
                self.__battery -= 5
                return f'Phrase Added'
            else:
                print("I know that one, teach me another phrase")
                phrase = input('>>> ')
        else:
            if self.power == "On":
                return f'Memory full'
            else:
                return f'...'

    def show_phrases(self):
        if self.power == "On":
            self.__battery -= 3
            print('I know these phrases:\n')
            for index in range(len(self.phrases)):
                print(f'|{index + 1}|{self.phrases[index]}|')
            return f'Done'
        else:
            return '...'

    def show_a_phrase(self, phrase_number):
        if self.power == 'On':
            self.__battery -= 3
            for index in range(len(self.phrases)):
                if index == phrase_number - 1:
                    return f'{self.phrases[index]}'
                else:
                    return f'Phrase not found!\nbe sure you put the right phrase number...'
        else:
            return '...'

