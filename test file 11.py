count = 0
while count < 3:
    print("Processing...")
    count += 1

while True:
    cmd = input("Type 'exit' to quit: \n")
    if cmd == "exit": 
        print("Shutting down.")
        break

while True:
    cmd = input("Type 'exit' to quit: \n")
    if cmd == "exit":
        print("Shutting down.")
        break

for i in range(1,5):
    print("Current value of i is:", i)

for i in range(-2, 10, 2):
    print("This is an even number between -2 and 10: ", i)

while True:
    age = input("Enter age: ")
    if age.isdigit():
        age = int(age)
        print("You are: ", age)
        break
    else:
        print("Invalid. Numbers only.")

while True:
    age = input("Enter age: ")
    if age.isdigit():
        age = int(age)
        print("Age accepted")
        break
    else: print("Invalid. Numbers only")
