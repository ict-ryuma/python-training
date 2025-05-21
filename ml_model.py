import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. CSV読み込み
df = pd.read_csv("ml_sample.csv")

# 2. カテゴリ変換（職業 → 数値に変換）
le = LabelEncoder()
df["職業"] = le.fit_transform(df["職業"])  # 例：営業→0、Pythonエンジニア→1...

# 3. 説明変数（X）と目的変数（y）を分ける
X = df[["年齢", "職業", "残業時間"]]  # 入力データ
y = df["退職"]                     # 予測したいもの

# 4. 学習データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. モデル作成と学習
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 6. 予測して精度を確認
y_pred = model.predict(X_test)
print("✅ 予測精度：", accuracy_score(y_test, y_pred))

# 7. 実際の予測も表示
print("\n▼ 予測結果")
print(pd.DataFrame({
    "実際": y_test.values,
    "予測": y_pred
}))
