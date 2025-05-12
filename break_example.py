people = [
    {"name": "田中 太郎", "age": 17},
    {"name": "山田 太郎", "age": 32},
    {"name": "佐藤 次郎", "age": 70}
]

print("🔍 最初に見つかった成人の情報：")

for person in people:
    if person["age"] >= 20:
        print(f'{person["name"]} さん（{person["age"]}歳）')
        break
