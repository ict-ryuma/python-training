people = [
    {"name": "田中 太郎", "age": 17},
    {"name": "山田 太郎", "age": 32},
    {"name": "佐藤 次郎", "age": 70}
]

print("📋 成人者リスト（未成年はスキップ）：")

for person in people:
    if person["age"] < 20:
        continue  # 未成年ならスキップ
    print(f'{person["name"]} さん（{person["age"]}歳）')
