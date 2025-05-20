def calculate_total_age(people):
    total_age = 0
    for person in people:
        total_age += person["年齢"]
    return total_age

people = [
    {"名前": "田中 一郎", "年齢": 25},
    {"名前": "佐藤 二郎", "年齢": 31},
    {"名前": "高橋 三郎", "年齢": 42}
]

total = calculate_total_age(people)

print(f"合計年齢：{total}歳")
print(f"人数：{len(people)}人")
