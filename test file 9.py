door = input("You are in a haunted house and need to escape. "
             "Pick door 1, 2 or 3: ")

if door == "1":
    book = input("You have now entered a library. Pick book 1, 2 or 3: ")
    if book == "1":
        print("You die.")
    elif book == "2":
        print("You find a secret passage and escape")
    elif book == "3":
        print("you die.")
    else:
        print("Please pick 1, 2 or 3")

elif door == "2":
    bowl = input("You enter a kitchen. Pick bowl 1, 2 or 3: ")
    if bowl == "1":
        print("You die ")
    elif bowl == "2":
        print("You die.")
    elif bowl == "3":
        print("You find a secret passage and escape")
    else:
        print("Please pick 1, 2 or 3")

elif door == "3":
    print(" you die.")
    
else:
    print("That's not a door.")
