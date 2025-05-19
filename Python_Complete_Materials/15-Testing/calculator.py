# Your code here
class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y
    
    def subtract(self, x,y):
        return x - y
    
    def multiplication(self, x,y):
        return x * y
    
    def division(self, x,y):
        try: 
            return x / y
        except ZeroDivisionError:
            return "You cannot divide by a zero!"
    
    def integer_division(self, x,y):
        try: 
            return x // y
        except ZeroDivisionError:
            return "You cannot divide by a zero! Please chose a different number."