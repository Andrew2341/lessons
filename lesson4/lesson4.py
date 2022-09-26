class Calculator:

    def __init__(self):
        self.last_sum = None

    def sum(self, a, b):
        sum = a + b
        self._set_last_sum(sum)
        return sum

    def _set_last_sum(self, sum):
        self.last_sum = sum

    def get_last_sum(self):
        return self.last_sum

# Конец класса

calc = Calculator()
# x = Calculator()
print(calc.get_last_sum())
print(calc.sum(2,2))
print(calc.get_last_sum())
print(calc.sum(3,2))
print(calc.get_last_sum())
print(calc._set_last_sum(7))
print(calc.get_last_sum())


# print(x.sum(3,3))
