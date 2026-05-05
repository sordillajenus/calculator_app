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
        return a / b

    def ask_numbers(self, a, b):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        return a, b