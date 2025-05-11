people = [
    {"name": "田中 太郎", "age": 32},
    {"name": "佐藤 花子", "age": 18},
    {"name": "鈴木 次郎", "age": 45},
    {"name": "高橋 美咲", "age": 17}
]

print("✅ 成人者一覧")
for person in people:
    if person["age"] >= 20:
        print(f'▶ {person["name"]} さん（{person["age"]}歳）')
