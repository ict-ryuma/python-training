import pandas as pd

# CSVを読み込む
df = pd.read_csv("people.csv")

# 「エンジニア」を含む行だけを抽出
engineers = df[df["職業"].str.contains("エンジニア")]

# クロス集計：職業 × 年齢
summary = engineers.groupby(["職業", "年齢"]).size()

# 表示する
for (job, age), count in summary.items():
    print(f"職業: {job} / 年齢: {age}歳 → {count}人")
