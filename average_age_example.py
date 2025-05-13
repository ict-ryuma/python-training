people = [
    {"名前": "田中 一郎", "年齢": 25},
    {"名前": "佐藤 二郎", "年齢": 31},
    {"名前": "高橋 三郎", "年齢": 42}
]

# 年齢の合計を求める
total_age = 0
for person in people:
    total_age += person["年齢"]

# 平均を求める
average_age = total_age / len(people)

print(f"人数：{len(people)}人")
print(f"平均年齢：{average_age:.1f}歳")
