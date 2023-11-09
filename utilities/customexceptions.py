class EmulatorNotFoundError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))

class SeriesNotFoundError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))



class PartNotFoundError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))


class GroupSelectionError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))

