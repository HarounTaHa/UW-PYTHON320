import adder, subtractor, multiplier, divider
from calculator import Calculator

calculator = Calculator(adder.Adder(), subtractor.Subtractor(), multiplier.Multiplier(), divider.Divider())
print(calculator.stack)
print(calculator.add())
