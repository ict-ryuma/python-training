# データの準備
people = [
    {"name": "田中", "age": 17},
    {"name": "山田", "age": 32},
    {"name": "佐藤", "age": 70}
]

# 条件付きループ：未成年はスキップして、成人以上だけにメッセージ表示
print("✅ 通知対象者一覧")
for person in people:
    if person["age"] < 20:
        continue  # 未成年は処理をスキップ

    print(f"{person['name']} さん（{person['age']}歳）に通知を送信します")
