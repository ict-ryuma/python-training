import csv

# 仮のデータ（例として使用）
cross_count = {
    ("開発", "若手"): 3,
    ("事業", "中堅"): 2,
    ("開発", "中堅"): 4,
    ("デザイン", "中堅"): 2,
    ("事業", "ベテラン"): 1,
    ("事業", "若手"): 1,
    ("デザイン", "若手"): 2
}

# 保存先ファイル名
filename = "cross_output.csv"

# ファイルに書き出し
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["職業カテゴリ", "年齢カテゴリ", "人数"])  # ヘッダー
    for (job_group, age_group), count in cross_count.items():
        writer.writerow([job_group, age_group, count])
