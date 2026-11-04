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

#This line has to return a 0 value for failed attempts if there is no
#set value for it already
failed_attempts = siem_logs.get('failed_attempts',0)

#Create a list for high risk users, then if the failed_attempts
#is a certain limit, add the user to that list
high_risk_users = []

for user_id in siem_logs.keys():
    print(user_id)

for user_id, data in siem_logs.items():
    failed_count = data["failed_attempts"]
    if failed_count > 5:
        high_risk_users.append(user_id)

print(high_risk_users)