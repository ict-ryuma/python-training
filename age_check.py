# 顧客データ（辞書のリスト）
customers = [
    {"name": "田中 花子", "age": 28, "score": 82},
    {"name": "山田 太郎", "age": 45, "score": 74},
    {"name": "鈴木 次郎", "age": 17, "score": 91}
]

# 表示する
print("=== 顧客情報 ===")
for customer in customers:
    print(f"{customer['name']}（{customer['age']}歳）- スコア: {customer['score']}")
