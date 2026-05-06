import math
import sympy
import statistics
from app_calculator import Calculator

class ScientificSymbolic(Calculator):
    
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
    
    def power(self, number_1, number_2):
        return math.pow(number_1, number_2)
    
    def factorial(self, number):
        return math.factorial(number)
    
    def derivative(self, expression):
        differential_quotient_dy_over_dx = sympy.Symbol("x")
        return sympy.diff(expression, differential_quotient_dy_over_dx)
    
    def integral(self, expression):
        differential_dx = sympy.Symbol("x")
        return sympy.integrate(expression, differential_dx)