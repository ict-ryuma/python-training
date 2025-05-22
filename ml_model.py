import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# データ読み込み
df = pd.read_csv("ml_sample.csv")

# ラベルエンコード
le_job = LabelEncoder()
le_gender = LabelEncoder()
le_divorce = LabelEncoder()

df["職業"] = le_job.fit_transform(df["職業"])
df["性別"] = le_gender.fit_transform(df["性別"])
df["離婚"] = le_divorce.fit_transform(df["離婚"])

# 特徴量と目的変数に分ける
X = df[["年齢", "職業", "残業時間", "性別", "離婚", "パワハラレベル"]]
y = df["退職"]

# 学習データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# モデル作成・学習
model = RandomForestClassifier()
model.fit(X_train, y_train)

# モデル・エンコーダを保存
joblib.dump(model, "model.pkl")
joblib.dump(le_job, "label_encoder.pkl")
