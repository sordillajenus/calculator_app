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
        choices = {}
        try:
            print("Scientific-Symbolic\n")
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            print("4. Cosecant")
            print("5. Secant")
            print("6. Cotangent")
            print("7. Logarithmic")
            print("8. Hypotenuse")
            print("9. Power")
            print("10. Factorial")
            print("11. Squareroot")
            print("12. Differentiation")
            print("13. Integration")

            operation = input("Enter your choice (1-13): ")
            if operation not in []



            
                              