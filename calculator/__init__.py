from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        calculations = Calculations(a, b, add)  # Pass the add function from calculator.operations
        return calculations.get_answer()
    @staticmethod
    def subtract(a,b):
        calculations = Calculations(a, b, subtract)  # Pass the subtract function from calculator.operations
        return calculations.get_answer()
    @staticmethod
    def multiply (a,b):
        calculations = Calculations(a, b, multiply)  # Pass the multiply function from calculator.operations
        return calculations.get_answer()
    @staticmethod
    def divide(a,b):
        calculations = Calculations(a, b, divide)  # Pass the divide function from calculator.operations
        return calculations.get_answer()