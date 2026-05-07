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
        return math.log(number)
    
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

            if not choice.isdigit() or not str(1 <= int(choice) <= len(choice)):
                raise ValueError("Plase Enter a Valid Choice.")
            return choice
        except ValueError("Enter a valid choice"):
            return self.ask_operation

    

            


            
                              