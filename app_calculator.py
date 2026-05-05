class Calculator:
    def __init__ (self):
        self.running = True

    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        
        return a / b

    def ask_numbers(self, a, b):
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            return a, b
        except ValueError:
            raise ValueError("The value you have entered is invalid")
        
    