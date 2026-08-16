class Comparison:

    def menu(self):
        while True:
            print("\n========== COMPARISON OPERATORS ==========")
            print("1. Equal (==)")
            print("2. Not Equal (!=)")
            print("3. Greater Than (>)")
            print("4. Less Than (<)")
            print("5. Greater Than or Equal (>=)")
            print("6. Less Than or Equal (<=)")
            print("7. Exit")
            print("==========================================")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 7:
                    print("Comparison calculator closed.")
                    break

                if choice < 1 or choice > 7:
                    print("Invalid choice. Please enter 1-7.")
                    continue

                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                if choice == 1:
                    self.Equal(a, b)

                elif choice == 2:
                    self.NotEqual(a, b)

                elif choice == 3:
                    self.GreaterThan(a, b)

                elif choice == 4:
                    self.LessThan(a, b)

                elif choice == 5:
                    self.GreaterThanOrEqual(a, b)

                elif choice == 6:
                    self.LessThanOrEqual(a, b)

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def Equal(self, a, b):
        print(f"{a} == {b} : {a == b}")

    def NotEqual(self, a, b):
        print(f"{a} != {b} : {a != b}")

    def GreaterThan(self, a, b):
        print(f"{a} > {b} : {a > b}")

    def LessThan(self, a, b):
        print(f"{a} < {b} : {a < b}")

    def GreaterThanOrEqual(self, a, b):
        print(f"{a} >= {b} : {a >= b}")

    def LessThanOrEqual(self, a, b):
        print(f"{a} <= {b} : {a <= b}")


# Object creation
comparison = Comparison()
comparison.menu()
