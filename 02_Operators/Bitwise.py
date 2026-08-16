class Bitwise:

    def menu(self):
        while True:
            print("\n========== BITWISE OPERATORS ==========")
            print("1. AND (&)")
            print("2. OR (|)")
            print("3. XOR (^)")
            print("4. NOT (~)")
            print("5. Left Shift (<<)")
            print("6. Right Shift (>>)")
            print("7. Exit")
            print("=======================================")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 7:
                    print("Bitwise operators closed.")
                    break

                if choice < 1 or choice > 7:
                    print("Invalid choice. Please enter 1-7.")
                    continue

                if choice == 4:
                    x = int(input("Enter a number: "))
                    self.Not(x)

                elif choice == 5 or choice == 6:
                    x = int(input("Enter the number: "))
                    y = int(input("Enter the number of positions: "))

                    if choice == 5:
                        self.LeftShift(x, y)
                    else:
                        self.RightShift(x, y)

                else:
                    x = int(input("Enter the first number: "))
                    y = int(input("Enter the second number: "))

                    if choice == 1:
                        self.And(x, y)

                    elif choice == 2:
                        self.Or(x, y)

                    elif choice == 3:
                        self.Xor(x, y)

            except ValueError:
                print("Invalid input. Please enter integers only.")

    def And(self, x, y):
        print(f"{x} & {y} : {x & y}")

    def Or(self, x, y):
        print(f"{x} | {y} : {x | y}")

    def Xor(self, x, y):
        print(f"{x} ^ {y} : {x ^ y}")

    def Not(self, x):
        print(f"~{x} : {~x}")

    def LeftShift(self, x, y):
        print(f"{x} << {y} : {x << y}")

    def RightShift(self, x, y):
        print(f"{x} >> {y} : {x >> y}")


# Object creation
bitwise = Bitwise()
bitwise.menu()
