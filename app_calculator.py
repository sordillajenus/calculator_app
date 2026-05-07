from scientific import ScientificSymbolic

class Calculator(ScientificSymbolic):

    def __init__(self):
        self.running = True

    def addition(self, number_1, number_2):
        return number_1 + number_2

    def subtraction(self, number_1, number_2):
        return number_1 - number_2

    def multiplication(self, number_1, number_2):
        return number_1 * number_2

    def division(self, number_1, number_2):
        if number_2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return number_1 / number_2

    def ask_numbers(self):
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            return number_1, number_2

        except ValueError:
            raise ValueError("The value you entered is invalid")

    def choose_operation(self):

        print("\nPlease Choose an Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice (1-4): ")

        if choice not in ["1", "2", "3", "4"]:
            raise ValueError("You must enter a valid choice")

        return choice

    def calculate(self):

        try:
            number_1, number_2 = self.ask_numbers()
            choice = self.choose_operation()

            if choice == "1":
                result = self.addition(number_1, number_2)

            elif choice == "2":
                result = self.subtraction(number_1, number_2)

            elif choice == "3":
                result = self.multiplication(number_1, number_2)

            elif choice == "4":
                result = self.division(number_1, number_2)

            print(f"\nResult: {result}")

        except Exception as error:
            print("Error:", error)

    def scientific_calculate(self):

        try:
            operations = self.ask_operation()
            value = self.ask_input(operations)

            result = self.calculate_scientific(operations, value)

            print(f"\nResult: {result}")

        except Exception as error:
            print("Error:", error)

    def calculate_scientific(self, operations, value):

        return super().calculate(operations, value)

    def repeat(self):

        question = input(
            "\nDo you want to try again? (yes/no): "
        ).lower()

        if question in ["no", "n"]:
            self.running = False

    def run(self):

        while self.running:

            try:
                choose = input(
                    "\nDo you want the:\n"
                    "1. Normal Calculator\n"
                    "2. Scientific Calculator\n"
                    "Enter choice (1/2): "
                )

                if choose not in ["1", "2"]:
                    raise ValueError("Invalid Choice")

                if choose == "1":
                    self.calculate()

                elif choose == "2":
                    self.scientific_calculate()

                if self.running:
                    self.repeat()

            except Exception as error:
                print("Error:", error)

        print("\nThank you for using the program")


calc = Calculator()
calc.run()