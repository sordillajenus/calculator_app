import math
import sympy

class ScientificSymbolic:

    def sine(self, number):
        return math.sin(math.radians(number))

    def cosine(self, number):
        return math.cos(math.radians(number))

    def tangent(self, number):
        return math.tan(math.radians(number))

    def cosecant(self, number):
        return 1 / math.sin(math.radians(number))

    def secant(self, number):
        return 1 / math.cos(math.radians(number))

    def cotangent(self, number):
        return 1 / math.tan(math.radians(number))

    def log(self, number):
        return math.log10(number)

    def hypotenuse(self, number_1, number_2):
        return math.hypot(number_1, number_2)

    def power(self, number_1, number_2):
        return math.pow(number_1, number_2)

    def factorial(self, number):
        return math.factorial(number)

    def squareroot(self, number):
        return math.sqrt(number)

    def derivative(self, expression):
        x = sympy.symbols("x")
        return sympy.diff(expression, x)

    def integral(self, expression):
        x = sympy.symbols("x")
        return sympy.integrate(expression, x)

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

        while True:
            choice = input("Please choose an operation (1-13): ").strip()

            if choice.isdigit() and 1 <= int(choice) <= len(operations):
                return operations[int(choice) - 1]

            print("Please enter a valid choice.")

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
                    return float(input("Enter a number: "))
                except ValueError:
                    print("Enter a valid input")

        elif operations == "Hypotenuse":
            while True:
                try:
                    number_1 = float(input("Enter first number: "))
                    number_2 = float(input("Enter second number: "))
                    return (number_1, number_2)
                except ValueError:
                    print("Enter valid numbers")

        elif operations == "Power":
            while True:
                try:
                    base = float(input("Enter the base: "))
                    exponent = float(input("Enter the exponent: "))
                    return (base, exponent)
                except ValueError:
                    print("Enter valid numbers")

        elif operations in symbolic_operations:
            return input(
                "Enter expression (use format x**2 + 3*x): "
            ).strip()

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
            return "Operation is not defined"

    def run(self):
        operations = self.ask_operation()
        value = self.ask_input(operations)
        result = self.calculate(operations, value)
        print(result)