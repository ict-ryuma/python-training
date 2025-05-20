import csv

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row["年齢"])
        
        # 年齢帯を分類
        if age <= 30:
            category = "若手"
        elif 31 <= age <= 45:
            category = "中堅"
        else:
            category = "ベテラン"

        print(f'{row["名前"]} さん（{age}歳）職業：{row["職業"]} ／ 区分：{category}')
