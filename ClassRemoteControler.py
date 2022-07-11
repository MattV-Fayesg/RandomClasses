from ClassTelevision import Television


class Remote(Television):

    def __init__(self, power=False, channel=1, volume=0, max_ch=999, max_vol=100):
        super().__init__(power, channel, volume, max_ch, max_vol)

    def channel_up(self):
        if self.max_ch > self.channel >= 1 and self.power == 'On':
            self.channel += 1
        elif self.max_ch <= self.channel and self.power == 'On':
            self.channel = 1
        for ch_name, ch_num in self.channel_list.items():
            if self.channel == ch_num:
                self.channel_name = ch_name
            else:
                self.channel_name = 'No signal'

    def channel_down(self):
        if self.max_ch >= self.channel > 1 and self.power == 'On':
            self.channel -= 1
        elif self.channel <= 1 and self.power == 'On':
            self.channel = self.max_ch
        for ch_name, ch_num in self.channel_list.items():
            if self.channel == ch_num:
                self.channel_name = ch_name
            else:
                self.channel_name = 'No signal'

    def vol_up(self):
        if self.max_vol > self.volume >= 0 and self.power == 'On':
            self.volume += 1
        elif self.max_vol <= self.volume and self.power == 'On':
            print(' VOL: 100%\n you cannot go higher than that\n')

    def vol_down(self):
        if self.max_vol >= self.volume > 0 and self.power == 'On':
            self.volume -= 1
        else:
            print(' VOL: 0%\n  you cannot go lower than that\n')

    def specific_ch(self, ch):
        for ch_name, ch_num in self.channel_list.items():
            if ch == ch_num:
                self.channel_name = ch_name
                self.channel = ch
                return f'Channel found!\n' \
                       f' {ch_name} | {ch}\n '
        else:
            return 'No signal'


# Running - Setting Object
tel = Remote(max_ch=3, max_vol=3)
print(tel.tv_status())
# Testing Turn it On
tel.turn_on()
print(tel.tv_status())
# Testing Turn it Off
tel.turn_off()
print(tel.tv_status())
# Testing Turning it off and increasing channel - Must not work
tel.channel_up()
print(tel.tv_status())
# Testing Turning it on and increasing channel - Must Work
tel.turn_on()
tel.channel_up()
print(tel.tv_status(), 'f')  # Ch = 3 (Limit tested)
tel.channel_up()  # Ch reset to 1
print(tel.tv_status())
# Testing Turning it on and decreasing channel - Must Work
tel.channel_down()
print(tel.tv_status())
# Testing Increasing channel to its limit
tel.channel_up()
tel.channel_up()
print(tel.tv_status(), 'f')  # Ch = 3 (Limit tested)
tel.channel_up()  # Ch reset to 1
print(tel.tv_status())

# Passing decreasing channel/volume passing its limits - test
tel.channel_down()
tel.vol_up()
print(tel.tv_status())
tel.channel_down()
tel.vol_down()
print(tel.tv_status())
tel.channel_down()
tel.vol_down()
print(tel.tv_status())
# Testing Channel List
tel.show_channel_list()
# Testing putting a specific channel -----------------
tel.specific_ch(135)
print(tel.tv_status())
# Testing Volume up limit ------------
tel.vol_up()
print(tel.tv_status())
tel.vol_up()
tel.vol_up()
print(tel.tv_status())  # Vol = 3 (Limit tested)
tel.vol_up()  # Vol warming message
print(tel.tv_status())
