import json
raw_json = '{"user": "Alice", "id": 101}'
data = json.loads(raw_json)  # Convert JSON string to Python dictionary

print(data)
#.keys, .values, and .items
for key in data.keys():
    print(f"Key: {key}")
for value in data.values():
    print(f"Value: {value}")
for key, value in data.items():
    print(f"Key-Value Pair: {key} : {value}")

raw_data = b'{"status":"success","data":{"user_id":1024,"username": "johndoe","email": "john@example.com","is_active": True,"roles": ["admin", "editor"],"profile": {"first_name": "John","last_name": "Doe","joined_date": "2026-11-09t15:30:00Z"}}}'

#1. Decode bytes to string
json_str = raw_data.decode("utf-8")

#2. Parse JSON string into a Python dictionary (loads handles true/false/null automatically)
data = json.loads(json_str)

#3. 

print(data.json)
