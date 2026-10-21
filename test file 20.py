## We are getting raw incident logs
    #Problem is, the raw logs are not in standard format, inconsistent whitespace, mixed
    #delimiters, which makes it harder for us (programemer) to handle the threat
##Our job is to write a script to clean the raw data, extract the malicious IP addresses,
##verify the firewall ports

# Define the immutable Tuple
# RAW SOCK SYSTEM LOGS
# Format: [Severity] | IP_ADDRESS | USERNAME | PORT | EVENT_STATUS

raw_forensic_logs = [
    " [critical] | 192.168.1.105 | Admin_User | 22 | failed_login ",
    " [WARNING] | 10.0.0.50 | root | 443 | MALWARE_SIGNATURE_DETECTED ",
    " [CRITICAL] | 172.16.254.1 | unknown_user | 80 | SQL_INJECTION_ATTEMPT ",
    " [alert] | 192.168.1.200 | SYS_ADMIN | 3389 | UNAUTHORIZED ACCESS ",
    " [warning] | 10.0.0.12 | test_acc | 8080 | brute_force_suspected ",
]


log_line_list = []
for line in raw_forensic_logs:
    sublist = line.split(" | ")
    log_line_list.append(sublist)

ip_list = []
for a in range(len(raw_forensic_logs)):
    ip_list.append(log_line_list[a][1])
print(ip_list)


#print(raw_forensic_logs[0])
#ip1 = raw_forensic_logs[0].split("|")
#print (ip1)
#ip2 = ip1[0].strip(" ")
#print (ip2)

#raw_log_size = len(raw_forensic_logs)
#print(raw_log_size)
#for a in range(raw_log_size):
#    raw_forensic_logs[a].split(" | ")
#    print(raw_forensic_logs[a])
#    a += 1