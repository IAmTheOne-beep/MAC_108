## We are getting raw incident logs
    #Problem is, the raw logs are not in standard format, inconsistent whitespace, mixed
    #delimiters, which makes it harder for us (programemer) to handle the threat
##Our job is to write a script to clean the raw data, extract the malicious IP addresses,
##verify the firewall ports

# Define the immutable Tuple
# RAW SOCK SYSTEM LOGS
# Format: [Severity] | IP_ADDRESS | USERNAME | PORT | EVENT_STATUS

# Lines 14-20 is our raw data logs, I want to create a list within a list


raw_forensic_logs = [
    " [critical] | 192.168.1.105 | Admin_User | 22 | failed_login ",
    " [WARNING] | 10.0.0.50 | root | 443 | MALWARE_SIGNATURE_DETECTED ",
    " [CRITICAL] | 172.16.254.1 | unknown_user | 80 | SQL_INJECTION_ATTEMPT ",
    " [alert] | 192.168.1.200 | SYS_ADMIN | 3389 | UNAUTHORIZED ACCESS ",
    " [warning] | 10.0.0.12 | test_acc | 8080 | brute_force_suspected ",
]
#I want to modify every line in the raw forensic log to be lowercased
lower_forensic_logs = []
for logline in raw_forensic_logs:
    sublist = logline.lower()
    lower_forensic_logs.append(sublist)

# Lines 24-27 created a new list, made of each entry within the raw data logs
log_line_list = []
for logline in lower_forensic_logs:
    sublist = logline.split(" | ")
    log_line_list.append(sublist)

#Lines 32-35 created an ip list
ip_list = []
for a in range(len(lower_forensic_logs)):
    ip_list.append(log_line_list[a][1])
print(ip_list)

user_list = []
for a in range(len(lower_forensic_logs)):
    user_list.append(log_line_list[a][2])
print(user_list)