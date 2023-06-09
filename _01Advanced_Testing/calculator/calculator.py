from exception import InsufficientOperands


class Calculator(object):
    def __init__(self, adder, subtractor, multiplier, divider):
        self.adder = adder
        self.subtractor = subtractor
        self.multiplier = multiplier
        self.divider = divider
        self.stack = []

    def enter_number(self, number):
        self.stack.insert(0, number)

    def _do_calc(self, operator):
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands
        self.stack = [result]
        return result

    def add(self):
        return self._do_calc(self.adder)

    def subtractor(self):
        return self._do_calc(self.subtractor)

    def multiply(self):
        return self._do_calc(self.multiplier)

    def divide(self):
        return self._do_calc(self.divider)
