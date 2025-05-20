import csv

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["年齢"]) <= 35:
            if "デザイナー" in row["職業"] or "エンジニア" in row["職業"]:
                print(f'{row["名前"]} さん（{row["年齢"]}歳）職業：{row["職業"]}')