import csv
from collections import defaultdict

# クロス集計のための辞書（初期値0）
cross_count = defaultdict(int)

# CSVファイルを開いて読み込む
with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row["年齢"])
        job = row["職業"]

        # 年齢カテゴリ
        if age <= 30:
            age_group = "若手"
        elif age <= 45:
            age_group = "中堅"
        else:
            age_group = "ベテラン"

        # 職業カテゴリ
        if "エンジニア" in job:
            job_group = "開発"
        elif "デザイナー" in job:
            job_group = "デザイン"
        else:
            job_group = "事業"

        # クロス集計（キーにタプルを使う）
        key = (job_group, age_group)
        cross_count[key] += 1

# CSVに保存
with open("cpractice_output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["名前", "年齢", "職業"])  # ヘッダー行
    for key, count in cross_count.items():
        writer.writerow([key[0], key[1], count])
