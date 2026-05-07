import math
import sympy
from app_calculator import Calculator

class ScientificSymbolic:
    
    def sine(self, number):
        return math.sin(number)
    
    def cosine(self, number):
        return math.cos(number)
    
    def tangent(self, number):
        return math.tan(number)
    
    def cosecant(self, number):
        return 1 / math.sin(number)
    
    def secant(self, number):
        return 1 / math.cos(number)
   
    def cotangent(self, number):
        return 1 / math.tan(number)

    def log(self, number):
        return math.log10(number)
    
    def hypotenuse(self, number_1, number_2):
        return math.hypot(number_1, number_2)
    
    def power(self, number_1, number_2):
        return math.pow(number_1, number_2)
    
    def factorial(self, number):
        return math.factorial(number)
    
    def squareroot(self, number):
        return math.sqrt(number )
    
    def derivative(self, expression):
        differential_quotient_dy_over_dx = sympy.Symbol("x")
        return sympy.diff(expression, differential_quotient_dy_over_dx)
    
    def integral(self, expression):
        differential_dx = sympy.Symbol("x")
        return sympy.integrate(expression, differential_dx)
    
    def ask_operation(self):
        operations = [
        "Sine", "Cosine", "Tangent", "Cosecant", "Secant", "Cotangent",
        "Logarithmic", "Hypotenuse", "Power", "Factorial", 
        "Squareroot", "Differentiation", "Integration"
        ]

        print("Scientific and Symbolic Calculator\n")
        print("Choose an operation\n")

        for i, name in enumerate(operations, 1):
            print(f"{i:2}. {name}")

        try:
            choice = input("Please choose an operation (1-13): ").strip()

            if not choice.isdigit() or not (1 <= int(choice) <= len(operations)):
                raise ValueError("Plase Enter a Valid Choice.")
            return operations[int(choice) - 1]
        
        except ValueError:
            return self.ask_operation()
        
    def ask_input(self, operations):

        numeric_operations = {
            "Sine", "Cosine", "Tangent",
            "Cosecant", "Secant", "Cotangent",
            "Logarithmic", "Hypotenuse", "Power",
            "Factorial", "Squareroot"
        }

        symbolic_operations = {
            "Differentiation", "Integration"
        }

        if operations in numeric_operations:
            while True:
                try:
                    number = float(input("Enter a number: "))
                    return number
                except ValueError:
                    print("Enter a valid input")

        elif operations == "Hypotenuse":
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            return (number_1, number_2)
        
        elif operations in symbolic_operations:
            expression = input(f"Enter expression or number for {operations} and use the format format x**2 + 3*x: ").strip()
            return expression


    def calculate(self, operations, value):

        if operations == "Sine":
            return math.sin(math.radians(value))
        
        elif operations == "Cosine":
            return math.cos(math.radians(value))
        
        elif operations == "Tangent":
            return math.tan(math.radians(value))
        
        elif operations == "Cosecant":
            return 1 / math.sin(math.radians(value))
        
        elif operations == "Secant":
            return 1 / math.cos(math.radians(value))
        
        elif operations == "Cotangent":
            return 1 / math.tan(math.radians(value))
        
        elif operations == "Hypotenuse":
            number_1, number_2 = value
            return math.hypot(number_1, number_2)
        
        elif operations == "Logarithmic":
            return math.log10(value)
        
        elif operations == "Squareroot":
            return math.sqrt(value)

        elif operations == "Factorial":
            return math.factorial(int(value))

        elif operations == "Power":
            base, exponent = value  
            return math.pow(base, exponent)
        
        elif operations == "Differentiation":
            differential_quotient_dy_over_dx = sympy.symbols('x')
            expression = sympy.sympify(value)
            return sympy.diff(expression, differential_quotient_dy_over_dx)

        elif operations == "Integration":
            differential_dx = sympy.symbols('x')
            expression = sympy.sympify(value)
            return sympy.integrate(expression, differential_dx)
        
        else:
            print("Operation is not defined")
                

    def run(self):
        operation = self.ask_operation()
        value = self.ask_input(operation)
        result = self.calculate(operation, value)
        print(result)
            
    

           

            


            
                              