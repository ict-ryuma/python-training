import csv
from collections import defaultdict

cross_count = defaultdict(int)

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row["年齢"])
        job = row["職業"]

        if age <= 30:
            age_group = "若手"
        elif age <= 45:
            age_group = "中堅"
        else:
            age_group = "ベテラン"

        if "エンジニア" in job:
            job_group = "開発"
        elif "デザイナー" in job:
            job_group = "デザイン"
        else:
            job_group = "事業"

        key = (job_group, age_group)
        cross_count[key] += 1

# CSVに保存
with open("cross_output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["職業カテゴリ", "年齢カテゴリ", "人数"])  # ヘッダー行
    for key, count in cross_count.items():
        writer.writerow([key[0], key[1], count])
