import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 5, 5) == 50

    def test_adding_multiply_correctly(self):
        assert self.calc.adding_multiply(self, 2, 2, 2) == 6

    def test_adding_multiply_failed(self):
        assert self.calc.adding_multiply(self, 2, 2, 2) == 20

    def test_adding_subtraction_multiply_correctly(self):
        assert self.calc.adding_subtraction_multiply(self, 5, 5, 2, 3) == 4

    def test_adding_subtraction_multiply_failed(self):
        assert self.calc.adding_subtraction_multiply(self, 5, 5, 2, 3) == 100
