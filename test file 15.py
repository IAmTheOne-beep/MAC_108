inventory = []

while True:
    choice = input("1: Add, 2: Remove, 3: View Inventory, 4: Check inventory number, 5: Exit\n")
    if choice == "1":
        item = input("Enter device to add: ")
        inventory.append(item)
    elif choice == "2":
        item = input("Enter device to remove: ")
        if item in inventory:
            inventory.remove(item)
        else:
            print("Item not found in inventory.")
    elif choice == "3":
        print("Current Inventory:", inventory)
    elif choice == "4":
        print("Which index would you like to check?")
        index = int(input())
        print("The item at index ", index, "is:", inventory[index])
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

