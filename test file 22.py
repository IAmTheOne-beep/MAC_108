# - 1. API returns JSON Payload (string)
# - 2. Python parses into Native Dictionary

import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
payload = response.json() # Converst JSON text to Python dictionary

# Accessing data via key-value looksups:
print(payload)
title = payload["title"]
print("Task title:", title)