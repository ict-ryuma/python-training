import csv
from collections import defaultdict

# 集計用の辞書（初期値0）
job_count = defaultdict(int)

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        job = row["職業"]
        job_count[job] += 1

# 結果を表示
print("🔍 職業ごとの人数集計結果：")
for job, count in job_count.items():
    print(f"{job}: {count}人")
