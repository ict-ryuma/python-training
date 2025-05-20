import pandas as pd

# CSV読み込み
df = pd.read_csv("eda_sample.csv")

# データの頭5行
print("▼ head(): データの最初の5件")
print(df.head())

# データの情報（行数・列・欠損など）
print("\n▼ info(): データ構造の概要")
print(df.info())

# 統計量の確認（数値列）
print("\n▼ describe(): 数値の要約統計")
print(df.describe())

import pandas as pd

df = pd.read_csv("eda_sample.csv")

# 性別ごとの人数（分布）
print("▼ 性別の分布（何人いるか）")
print(df["性別"].value_counts())

# 職業ごとの人数
print("\n▼ 職業の分布（何人いるか）")
print(df["職業"].value_counts())

# 職業ごとの平均年収
print("\n▼ 職業ごとの平均年収")
print(df.groupby("職業")["年収"].mean())

# 性別ごとの平均年収
print("\n▼ 性別ごとの平均年収")
print(df.groupby("性別")["年収"].mean())
