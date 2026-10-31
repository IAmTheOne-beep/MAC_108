#We are getting a server log
#We want to test if the server ip address is restricted

banned_ips = ["192.168.4.11", "192.168.4.12", "192.168.4.13", "192.168.4.14"]

raw_log = "ALERT | 2026-10-19 | 192.168.4.12 | SQL_Injection_Attempt"

clean_log = raw_log.split(" | ")

print(clean_log)
