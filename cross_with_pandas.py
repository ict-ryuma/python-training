import pandas as pd

# CSV読み込み
df = pd.read_csv("people.csv")

# 年齢カテゴリを追加
def age_group(age):
    if age <= 30:
        return "若手"
    elif age <= 45:
        return "中堅"
    else:
        return "ベテラン"

df["年齢カテゴリ"] = df["年齢"].apply(age_group)

# 職業カテゴリを追加
def job_group(job):
    if "エンジニア" in job:
        return "開発"
    elif "デザイナー" in job:
        return "デザイン"
    else:
        return "事業"

df["職業カテゴリ"] = df["職業"].apply(job_group)

# クロス集計（pivot_tableでもOK）
summary = df.groupby(["職業カテゴリ", "年齢カテゴリ"]).size().reset_index(name="人数")

# 表示
print(summary)
