def get_max_age(people):
    max_age = 0
    max_name = ""  # ← ここが必要！
    for person in people:
        if person["年齢"] > max_age:
            max_age = person["年齢"]
            max_name = person["名前"]  # ← 名前も記録！
    return max_age, max_name

# データ
people = [
    {"名前": "田中 一郎", "年齢": 25},
    {"名前": "佐藤 二郎", "年齢": 31},
    {"名前": "高橋 三郎", "年齢": 42}
]

# 関数を使って最大年齢を取得
max_age, name = get_max_age(people)

print(f"最大年齢：{max_age}歳／名前：{name}さん")
