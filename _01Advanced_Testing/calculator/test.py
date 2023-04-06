from unittest import TestCase
from adder import Adder
from unittest.mock import MagicMock
from multiplier import Multiplier
from divider import Divider
from \
    subtractor import Subtractor
from calculator import Calculator
from exception import InsufficientOperands


class AdderTests(TestCase):
    def test_adding(self):
        adder = Adder()
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtractorTests(TestCase):
    def test_adding(self):
        subtractor = Subtractor()
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtractor.calc(i, j))


class CalculatorTests(TestCase):
    def setUp(self):
        self.adder = Adder()
        self.subtractor = Subtractor()
        self.multiplier = Multiplier()
        self.divider = Divider()
        self.calculator = Calculator(self.adder, self.subtractor, self.multiplier, self.divider)

    def test_insufficient_operands(self):
        self.calculator.enter_number(0)
        with self.assertRaises(InsufficientOperands):
            self.calculator.add()

    def test_adder_call(self):
        self.adder.calc = MagicMock(return_value=0)
        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.add()
        self.adder.calc.assert_called_with(1, 2)

    def test_subtractor_call(self):
        self.subtractor.calc = MagicMock(return_value=0)
        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.subtractor()
        self.subtractor.calc.assert_called_with(1, 2)
