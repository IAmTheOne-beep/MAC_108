#Our job is to remove leading and trailing whitespace for flagged username
#Convert all characters to lowercase
#Output a clean, standardized username

users = []
while True:
    user_input = input("Enter your username to be cleaned. Type 2 to exit \n")
    if user_input == "2":
        break
    else:
        clean_username = user_input.strip().lower().replace(" ", "")
        users.append(clean_username)
        print(users)