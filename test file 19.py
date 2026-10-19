#We are getting a server log
#We want to test if the server ip address is restricted

banned_ips = ["192.168.4.11", "192.168.4.12", "192.168.4.13", "192.168.4.14"]

raw_log = "ALERT | 2026-10-19 | 192.168.4.12 | SQL_Injection_Attempt"

clean_log = raw_log.split(" | ")
print(clean_log)
log_size = len(clean_log)
a = 0
while a < log_size:
    if a == 0:
        print("Log Type: " + clean_log[a])
    elif a == 1:
        print("Log Date: " + clean_log[a])
    elif a == 2:
        print("IP Address: " + clean_log[a])
    elif a == 3:
        print("Log Message: " + clean_log[a])
    a += 1

if clean_log[2] in banned_ips:
    print("Alert: Banned IP detected! \n" \
    "You have been blocked!")
else:
    print("IP is allowed.")