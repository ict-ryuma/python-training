import csv
from collections import defaultdict

# クロス集計用の辞書（キー：職業 × 年齢、値：人数）
cross_count = defaultdict(int)

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row["年齢"])
        job = row["職業"]

        # 年齢カテゴリを分類
        if age <= 30:
            age_group = "若手"
        elif 31 <= age <= 45:
            age_group = "中堅"
        else:
            age_group = "ベテラン"

        # 職業カテゴリを分類
        if "エンジニア" in job:
            job_group = "開発"
        elif "デザイナー" in job:
            job_group = "デザイン"
        else:
            job_group = "事業"

        # cross_count のキーをタプルにする
        key = (job_group, age_group)
        cross_count[key] += 1

# 結果を表示
print("【職業 × 年齢区分】集計結果：\n")
for key, count in cross_count.items():
    print(f"{key[1]:<6} × {key[0]:<6}：{count}人")

