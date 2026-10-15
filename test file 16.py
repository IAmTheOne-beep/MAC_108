approved_models = ("Macbook pro", "Dell XP", "Lenovo ThinkPad", "HP Spectre")
device_inventory = []


while True:
    print(
    "1. Add Device \n" \
    "2. Remove Device \n" \
    "3. View Inventory \n" \
    "4. Exit")
    choice = input("Choose an option. :")
    if choice == "1":
        newdevice = input("Enter the device name to add: ")
        if newdevice in approved_models:
            device_inventory.append(newdevice)
            print(f"{newdevice} has been added to the inventory.")
        else:
            print(f"{newdevice} is not an approved model. Please choose from the approved models: {', '.join(approved_models)}")
    elif choice == "2":
        olddevice = input("Enter the device name to remove: ")
        if olddevice in device_inventory:
            device_inventory.remove(olddevice)
            print(f"{olddevice} has been removed from the inventory.")  
    elif choice == "3":
        print("Current Inventory: ", device_inventory)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")