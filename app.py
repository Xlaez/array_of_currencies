import json

with open('names.json', 'r') as file:
    data = json.load(file)

currencies = []

for code, name in data.items():
    currencies.append(code)

print(currencies)