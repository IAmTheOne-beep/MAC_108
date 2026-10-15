secret_pin = "4444"
attempt = 0
while attempt < 3:
    guess = input("Enter pin:\n")
    if guess == secret_pin:
        print("Correct pin. Your balance is $5000.")
        break
    else:
        print("Incorrect pin. Please try again.")
        attempt +=1
        if attempt == 3:
            print("Too many attempts, Locked out.")
            break