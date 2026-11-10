##We are going to process and analyze logs from a system.
##We are going to automate the workflow, using nested dictionaries and mimic structure of JSON payloads.
##Task 1: Identify attack signatures by iterating through nested data structures.
##Task 2: Safely handle log entries without crashing
##Task 3: Enrich existing datasets with new security compliance flags.
##Understand how to use .items(), .values(), .get() to solve challenges.

siem_logs = {
    "user_001": {
        "username": "jdoe",
        "status": "active",
        "failed_attempts": 1},
    "user_002": {
        "username": "rsmith",
        "status": "locked",
        "failed_attempts": 15},
    "user_003": {
        "username": "tjones",
        "status": "active",
        "failed_attempts": 0},
    "user_004": {
        "username": "bwayne",
        "status": "active",}
        ##Missing attempt key, we will handle this
}   

#Create a list for high risk users, then if the failed_attempts
#is a certain limit, add the user to that list
high_risk_users = []

#We get the failed attempts for each user, if the key is missing, we will return a default value of 0
for user_id, data in siem_logs.items():
    failed_attempts = data.get("failed_attempts", 0)

    #If the failed attemps is greater than 5, we make sure status is locked
    if failed_attempts > 5:
        data["status"] = "locked"
        high_risk_users.append(user_id)

        #We want to get the value for the username per user id, if there is no username,
        #We return an unknown username string so it doesn't crash
        username = data.get("username", "Unknown User")
        print("Account locked for user:\n",username)

print("High risk users:\n",high_risk_users)

#We want to add a new key value pair to the logs
for data in siem_logs.values():
    data["2FA_enabled"] = True

for user_id, data in siem_logs.items():
    print("User ID:",{user_id}, "2FA Enabled:",{data['2FA_enabled']})

