#Our job is to remove leading and trailing whitespace for flagged username
#Convert all characters to lowercase
#Output a clean, standardized username

users = []
user_input = "AdminUser_99"

clean_username = user_input.strip()
clean_username = clean_username.lower()
users.append(clean_username)
print(users)
