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
        
    def choose_operation(self):
        print("Please Choose an Operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice (1-4): ")

        if choice not in ["1", "2", "3", "4"]:
            raise ValueError("You must enter a valid choice")
        
    def calculate(self):
        try:
            choice = self.choose_operation()
            a, b = self.ask_numbers()

            if choice == "1":
                result = self.addition(a, b)


        
    