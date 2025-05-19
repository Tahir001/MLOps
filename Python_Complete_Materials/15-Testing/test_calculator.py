from calculator import Calculator
import pytest

class TestCalculator:

    def setup_method(self):
        self.calculator = Calculator()
    
    def test_add(self):
        assert self.calculator.add(10, 5) == 15
        assert self.calculator.add(100,200) == 300
        assert self.calculator.add(100,2000) == 2100
        assert self.calculator.add(1,2) == 3
    
    def test_subtract(self):
        assert self.calculator.subtract(10, 5) == 5

    def test_multiplication(self):
        assert self.calculator.multiplication(10, 5) == 50
    
    def test_division(self):
        assert self.calculator.division(10, 5) == 2
    
    def test_integer_division(self):
        assert self.calculator.integer_division(10, 5) == 2
        assert self.calculator.integer_division(10, 0) == "You cannot divide by a zero! Please chose a different number."