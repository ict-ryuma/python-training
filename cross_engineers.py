import csv
from collections import defaultdict

# 集計用の入れ物（辞書の中に辞書）
summary = defaultdict(lambda: defaultdict(int)) # 初期値を0とカウントする

# CSVファイルを読み込む
with open("people.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if "エンジニア" in row["職業"]:
            job = row["職業"] # 列として代入する
            age = row["年齢"]
            summary[job][age] += 1 # カウントしたら1を足していく

# 結果を表示する
for job, ages in summary.items():
    print(f"職業: {job}")
    for age, count in ages.items():
        print(f"  年齢: {age}歳 → {count}人")