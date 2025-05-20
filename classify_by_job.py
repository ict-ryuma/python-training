import csv

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        job = row["職業"]
        age = row["年齢"]

        # 職業を分類
        if "エンジニア" in job:
            category = "開発"
        elif "デザイナー" in job:
            category = "デザイン"
        else: 
            category = "事業"

        print(f'{row["名前"]} さん（{age}歳）職業：{row["職業"]} ／ 区分：{category}')
