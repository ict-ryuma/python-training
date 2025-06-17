import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 日本語対応（任意）
matplotlib.rcParams['font.family'] = 'AppleGothic'

# モデルとエンコーダの読み込み
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# データ読み込み
df = pd.read_csv("ml_sample.csv")

# エンコード処理
df["職業"] = label_encoder.transform(df["職業"])
df["性別"] = df["性別"].map({"男性": 0, "女性": 1})
df["離婚"] = df["離婚"].map({"なし": 0, "あり": 1})

# 特徴量
X = df[["年齢", "職業", "残業時間", "性別", "離婚", "パワハラレベル"]]

# SHAP計算
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# SHAP平均値（2クラス平均も取る）
mean_shap = np.abs(shap_values).mean(axis=0).mean(axis=1)

# プロット
plt.figure(figsize=(8, 6))
plt.bar(X.columns, mean_shap)
plt.xlabel("SHAP value（平均絶対値）")
plt.title("特徴量の重要度（SHAP棒グラフ）")
plt.tight_layout()
plt.savefig("shap_summary_bar_forced.png", bbox_inches="tight")
plt.close()
