customers = [
    {"name": "田中 花子", "overdue_days": 0},
    {"name": "山田 太郎", "overdue_days": 7},
    {"name": "鈴木 次郎", "overdue_days": 3},
]

for customer in customers:
    print(f"確認中：{customer['name']}")
    if customer["overdue_days"] > 5:
        print(f"▶ {customer['name']} さんは支払い遅延（{customer['overdue_days']}日）！通知送信 ✅")
        break
