import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# ---------------------------
# 学習フェーズ
# ---------------------------

# 学習用データ読み込み
df = pd.read_csv("ml_sample.csv")

# ラベルエンコーディング（職業→数字）
le = LabelEncoder()
df["職業"] = le.fit_transform(df["職業"])

# 説明変数と目的変数
X = df[["年齢", "職業", "残業時間"]]
y = df["退職"]

# モデル学習
model = RandomForestClassifier()
model.fit(X, y)

# ---------------------------
# 予測フェーズ（ここアプリっぽく！）
# ---------------------------

# 入力データ（←ここを書き換えれば、別の人でも予測できる！）
new_data = pd.DataFrame([{
    "年齢": 24,
    "職業": le.transform(["Pythonエンジニア"])[0],
    "残業時間": 50
}])

# 予測
prediction = model.predict(new_data)[0]
label = "退職する可能性が高いです 💩" if prediction else "退職しない可能性が高いです 💪"

# 結果表示
print("▼ 入力されたユーザー情報：")
print(new_data)
print("\n▼ AIからの予測結果：")
print(label)
