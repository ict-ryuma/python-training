people = [
    {"name": "田中 太郎", "age": 32, "job": "エンジニア"},
    {"name": "佐藤 花子", "age": 45, "job": "デザイナー"},
    {"name": "鈴木 次郎", "age": 19, "job": "学生"},
    {"name": "山田 三郎", "age": 55, "job": "エンジニア"},
]

print("✅ ベテランエンジニア一覧（30歳以上かつエンジニア）")

for person in people:
    if person["age"] >= 30 and person["job"] == "エンジニア":
        print(f'{person["name"]} さん（{person["age"]}歳 / {person["job"]}）')
