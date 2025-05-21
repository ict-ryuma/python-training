import pandas as pd

# データを読み込む
df = pd.read_csv("ml_sample.csv")

# データの構造を確認
print("▼ データの最初の5行")
print(df.head())

print("\n▼ 情報（データ型・欠損など）")
print(df.info())

print("\n▼ 数値の統計情報")
print(df.describe())

print("\n▼ カテゴリ値の一覧（職業）")
print(df["職業"].value_counts())
