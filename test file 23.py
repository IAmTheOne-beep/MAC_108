class NetworkScanner:
	def __init__(self, name):
		self.tool_name = name

s1 = NetworkScanner('PortScanner')

print(s1.tool_name)

log_entry = {
	"ip": "192.168.1.105",
	"status": 401,
	"user": "admin"
}

for key in log_entry.keys():
	print(f"These are the keys in the log_entry: {key}")

for value in log_entry.values():
	print(f"These are the values in the log_entry: {value}")

for key, value in log_entry.items():
	print(f"These are the key-value pairs in the log_entry: {key} : {value}")
	