class Arithmetic:

    def menu(self):
        while True:
            print("\n========== ARITHMETIC OPERATORS ==========")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulus (Remainder)")
            print("6. Power")
            print("7. Floor Division")
            print("8. Exit")
            print("==========================================")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 8:
                    print("Calculator closed.")
                    break

                if choice < 1 or choice > 8:
                    print("Invalid choice. Please enter 1-8.")
                    continue

                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                if choice == 1:
                    self.Addition(a, b)

                elif choice == 2:
                    self.Subtraction(a, b)

                elif choice == 3:
                    self.Multiplication(a, b)

                elif choice == 4:
                    self.Division(a, b)

                elif choice == 5:
                    self.Modulus(a, b)

                elif choice == 6:
                    self.Power(a, b)

                elif choice == 7:
                    self.FloorDivision(a, b)

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def Addition(self, a, b):
        print(f"Addition: {a + b}")

    def Subtraction(self, a, b):
        print(f"Subtraction: {a - b}")

    def Multiplication(self, a, b):
        print(f"Multiplication: {a * b}")

    def Division(self, a, b):
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Division: {a / b}")

    def Modulus(self, a, b):
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Modulus: {a % b}")

    def Power(self, a, b):
        print(f"Power: {a ** b}")

    def FloorDivision(self, a, b):
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Floor Division: {a // b}")
# Object creation
calculator = Arithmetic()
calculator.menu()