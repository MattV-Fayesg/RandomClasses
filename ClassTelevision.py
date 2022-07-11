from ClassAppliance import Appliance


class Television(Appliance):

    def __init__(self, power=False, channel=1, volume=0, max_ch=999, max_vol=100):
        super().__init__(power)
        self.__channel = channel
        self.__volume = volume
        self.__max_ch = max_ch
        self.__max_vol = max_vol
        self.__channel_name = 'No signal'
        self.__channel_list = {'DisneyXD': 135, 'Cartoon Network': 58, 'Star': 199, 'BBC': 2, 'TVS': 42}

    @property
    def channel_name(self):
        return self.__channel_name

    @property
    def channel(self):
        return self.__channel

    @property
    def max_ch(self):
        return self.__max_ch

    @property
    def volume(self):
        return self.__volume

    @property
    def max_vol(self):
        return self.__max_vol

    @property
    def channel_list(self):
        return self.__channel_list

    @channel_name.setter
    def channel_name(self, name):
        self.__channel_name = name

    @channel.setter
    def channel(self, ch):
        self.__channel = ch

    @max_ch.setter
    def max_ch(self, mch):
        self.__max_ch = mch

    @volume.setter
    def volume(self, vol):
        self.__volume = vol

    @max_vol.setter
    def max_vol(self, mvl):
        self.__max_vol = mvl

    def show_channel_list(self):
        print(f'\nChannel List')
        for ch_name, num in self.channel_list.items():
            print(f' Channel name: {ch_name}|\n  Channel num: {num}\n -------')
        print('')

    def tv_status(self):
        return f'Tv Status\n' \
               f' On/Off: {self.power}\n' \
               f' Channel: {self.channel_name} | {self.channel}\n' \
               f' Volume: {self.volume}\n' \
               f' Max vol possible: {self.max_vol} | Max ch possible: {self.max_ch}\n'
