people = [
    {"name": "田中", "age": 17},
    {"name": "山田", "age": 24},
    {"name": "佐藤", "age": 70},
]

for person in people:
    if person["age"] < 20:
        print(f"{person['name']} さんは未成年です")
    elif person["age"] >= 65:
        print(f"{person['name']} さんはシニアです")
    else:
        print(f"{person['name']} さんは成人です")
