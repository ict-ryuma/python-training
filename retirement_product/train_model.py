# train_model.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import HistGradientBoostingClassifier
import joblib

# データ読み込み
df = pd.read_csv("ml_sample.csv")

# エンコード処理
le_job = LabelEncoder()
le_gender = LabelEncoder()
le_divorce = LabelEncoder()

df["職業"] = le_job.fit_transform(df["職業"])
df["性別"] = le_gender.fit_transform(df["性別"])
df["離婚"] = le_divorce.fit_transform(df["離婚"])
df["退職"] = df["退職"].astype(int)

# 特徴量と目的変数
X = df[["年齢", "職業", "残業時間", "性別", "離婚", "パワハラレベル"]]
y = df["退職"]

# モデル学習
model = HistGradientBoostingClassifier().fit(X, y)

# モデルとエンコーダの保存
joblib.dump(model, "model.pkl")
joblib.dump(le_job, "le_job.pkl")
joblib.dump(le_gender, "le_gender.pkl")
joblib.dump(le_divorce, "le_divorce.pkl")
