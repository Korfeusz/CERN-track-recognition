import random
from abc import ABC, abstractmethod


class Parameter(ABC):
    def __init__(self, value=None):
        self.value = value

    @abstractmethod
    def choose_random(self):
        pass


class FloatParameter(Parameter):
    def choose_random(self):
        try:
            return random.uniform(*self.value)
        except TypeError:
            print("Input value should be tuple, not {}".format(type(self.value)))
            return None


class IntParameter(Parameter):
    def choose_random(self):
        try:
            return random.randint(*self.value)
        except TypeError:
            print("Input value should be tuple, not {}".format(type(self.value)))
            return None


class MultipleChoiceParameter(Parameter):
    def __init__(self, size, fixed_size, value=None):
        self.size = size
        self.fixed_size = fixed_size
        super().__init__(value)

    def choose_random(self):
        if not self.fixed_size:
            if type(self.size) == tuple:
                size = random.randint(*self.size)
            else:
                try:
                    size = random.randint(1, self.size)
                except TypeError:
                    print("Size should be tuple or int not {}".format(type(self.size)))
                    return None
        else:
            size = self.size
        try:
            return random.sample(self.value, size)
        except TypeError:
            print("Wrong parameter types")
            return None


class SingleChoiceParameter(MultipleChoiceParameter):
    def __init__(self, value=None):
        super().__init__(size=1, fixed_size=True, value=value)

    def choose_random(self):
        try:
            return super().choose_random().pop()
        except AttributeError:
            return None
