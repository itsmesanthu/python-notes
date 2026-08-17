def add():
    cid = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    address = input("Enter Customer Address: ")
    contact = input("Enter Contact Number: ")
    
    with open("customer.txt", "a") as f:
        f.write(cid + "\t" + name + "\t" + address + "\t" + contact + "\n")
    print("Record added successfully!\n")


def show():
    print("-" * 40)
    print("ID\tName\tAddress\tContact")
    print("-" * 40)
    try:
        with open("customer.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No records found (file does not exist yet).\n")


def search():
    target_id = input("Enter the ID to be searched from file: ")
    found = False
    try:
        with open("customer.txt", "r") as f:
            all_records = f.readlines()
            for data in all_records:
                d = data.split("\t", 1)
                if d[0] == target_id:
                    print("-" * 40)
                    print("Record Found:")
                    print("ID\tName\tAddress\tContact")
                    print("-" * 40)
                    print(data)
                    found = True
                    break
        if not found:
            print("Record not found.\n")
    except FileNotFoundError:
        print("File does not exist yet.\n")


def delete():
    target_id = input("Enter the ID to remove from the file: ")
    try:
        with open("customer.txt", "r") as f:
            all_records = f.readlines()
            
        with open("customer.txt", "w") as f:
            for data in all_records:
                d = data.split("\t", 1)
                if d[0] != target_id:
                    f.writelines(data)
                    
        print("Record deleted (if it existed).\n")
    except FileNotFoundError:
        print("File does not exist yet.\n")


def update():
    target_id = input("Enter the ID to be updated from the file: ")
    try:
        with open("customer.txt", "r") as f:
            all_records = f.readlines()
            
        with open("customer.txt", "w") as f:
            for data in all_records:
                d = data.split("\t", 1)
                if d[0] == target_id:
                    new_name = input("Enter New Name: ")
                    new_address = input("Enter New Address: ")
                    new_contact = input("Enter New Contact Number: ")
                    f.writelines(d[0] + "\t" + new_name + "\t" + new_address + "\t" + new_contact + "\n")
                else:
                    f.writelines(data)
                    
        print("Record updated successfully.\n")
    except FileNotFoundError:
        print("File does not exist yet.\n")


# Main Program Loop
while True:
    print("Welcome to Customer Portal")
    print("1. Add new customer")
    print("2. Delete customer")
    print("3. Update customer")
    print("4. Search customer")
    print("5. Show all customers")
    print("6. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        add()
    elif ch == 2:
        delete()
    elif ch == 3:
        update()
    elif ch == 4:
        search()
    elif ch == 5:
        show()
    elif ch == 6:
        print("Exiting application...")
        break
    else:
        print("Invalid choice! Please try again.\n")