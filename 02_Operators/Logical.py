class Logical:

    def menu(self):
        while True:
            print("\n========== LOGICAL OPERATORS ==========")
            print("1. AND (and)")
            print("2. OR (or)")
            print("3. NOT (not)")
            print("4. Exit")
            print("=======================================")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 4:
                    print("Logical operators closed.")
                    break

                if choice < 1 or choice > 4:
                    print("Invalid choice. Please enter 1-4.")
                    continue

                # Take boolean input
                x = input("Enter first value (True/False): ").capitalize() == "True"

                if choice != 3:
                    y = input("Enter second value (True/False): ").capitalize() == "True"

                if choice == 1:
                    self.And(x, y)

                elif choice == 2:
                    self.Or(x, y)

                elif choice == 3:
                    self.Not(x)

            except ValueError:
                print("Invalid input.")


    def And(self, x, y):
        print(f"{x} and {y} : {x and y}")


    def Or(self, x, y):
        print(f"{x} or {y} : {x or y}")


    def Not(self, x):
        print(f"not {x} : {not x}")


# Object creation
logical = Logical()
logical.menu()