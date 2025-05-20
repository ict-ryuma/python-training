def get_min_age(people):
    min_age = 150  # 初期値は十分大きい数にしておく
    min_name = ""
    for person in people:
        if person["年齢"] < min_age:
            min_age = person["年齢"]
            min_name = person["名前"]
    return min_age, min_name


# データ
people = [
    {"名前": "田中 一郎", "年齢": 25},
    {"名前": "佐藤 二郎", "年齢": 31},
    {"名前": "高橋 三郎", "年齢": 42}
]

# 関数で最小年齢を取得
min_age, name = get_min_age(people)

print(f"最小年齢：{min_age}歳／名前：{name}さん")
