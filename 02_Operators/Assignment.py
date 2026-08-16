class Assignment:

    def menu(self):
        while True:
            print("\n========== ASSIGNMENT OPERATORS ==========")
            print("1. += Addition Assignment")
            print("2. -= Subtraction Assignment")
            print("3. *= Multiplication Assignment")
            print("4. /= Division Assignment")
            print("5. %= Modulus Assignment")
            print("6. **= Power Assignment")
            print("7. //= Floor Division Assignment")
            print("8. Exit")
            print("===========================================")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 8:
                    print("Assignment operators closed.")
                    break

                if choice < 1 or choice > 8:
                    print("Invalid choice. Please enter 1-8.")
                    continue

                c = float(input("Enter the initial value: "))
                value = float(input("Enter the value: "))

                if choice == 1:
                    self.AdditionAssignment(c, value)

                elif choice == 2:
                    self.SubtractionAssignment(c, value)

                elif choice == 3:
                    self.MultiplicationAssignment(c, value)

                elif choice == 4:
                    self.DivisionAssignment(c, value)

                elif choice == 5:
                    self.ModulusAssignment(c, value)

                elif choice == 6:
                    self.PowerAssignment(c, value)

                elif choice == 7:
                    self.FloorDivisionAssignment(c, value)

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def AdditionAssignment(self, c, value):
        print("Initial c:", c)
        c += value
        print(f"c += {value} :", c)

    def SubtractionAssignment(self, c, value):
        print("Initial c:", c)
        c -= value
        print(f"c -= {value} :", c)

    def MultiplicationAssignment(self, c, value):
        print("Initial c:", c)
        c *= value
        print(f"c *= {value} :", c)

    def DivisionAssignment(self, c, value):
        if value == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Initial c:", c)
            c /= value
            print(f"c /= {value} :", c)

    def ModulusAssignment(self, c, value):
        if value == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Initial c:", c)
            c %= value
            print(f"c %= {value} :", c)

    def PowerAssignment(self, c, value):
        print("Initial c:", c)
        c **= value
        print(f"c **= {value} :", c)

    def FloorDivisionAssignment(self, c, value):
        if value == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Initial c:", c)
            c //= value
            print(f"c //= {value} :", c)


# Object creation
assignment = Assignment()
assignment.menu()