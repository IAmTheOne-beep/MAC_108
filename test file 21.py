raw_forensic_logs = [
    " [critical] | 192.168.1.105 | Admin_User | 22 | failed_login ",
    " [WARNING] | 10.0.0.50 | root | 443 | MALWARE_SIGNATURE_DETECTED ",
    " [CRITICAL] | 172.16.254.1 | unknown_user | 80 | SQL_INJECTION_ATTEMPT ",
    " [alert] | 192.168.1.200 | SYS_ADMIN | 3389 | UNAUTHORIZED ACCESS ",
    " [warning] | 10.0.0.12 | test_acc | 8080 | brute_force_suspected ",
]

log_lines = []

for subline in raw_forensic_logs:
    sublist = subline.split(" | ")
    log_lines.append(sublist)

print (log_lines)