import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

# モデルとデータの読み込み
model = joblib.load("model/retention_model.pkl")
df = pd.read_csv("survey_responses/2025-05_summary.csv")

# 入力特徴量だけを抽出（不要な列は除外）
features = df.drop(columns=["comment", "要約", "感情"])

# SHAP値の計算
explainer = shap.Explainer(model.predict, features)
shap_values = explainer(features)

# SHAP要約プロット（特徴量の重要度）
shap.plots.bar(shap_values, max_display=10)
