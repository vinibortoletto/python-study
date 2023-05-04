class Tv:
    def __init__(self, size):
        self._volume = 50
        self._channel = 1
        self._size = size
        self._is_on = False

    def turn_volume_up(self):
        self._volume += 1

    def turn_volume_down(self):
        self._volume -= 1

    def change_channel(self, new_channel):
        if not 1 <= new_channel <= 99:
            raise ValueError

        self._channel = new_channel

    def turn_on_off(self):
        self._is_on = not self._is_on
