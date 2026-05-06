import math
import sympy
import statistics
from app_calculator import Calculator

class ScientificSymbolic(Calculator):
    
    def sine(self, x):
        return math.sin(x)
    
    def log(self, x):
        return math.log(x)
    
    def power(self, x, y):
        return math.pow(x, y)
    
    def factorial()