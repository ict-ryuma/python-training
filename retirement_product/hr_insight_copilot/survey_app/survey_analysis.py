import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
from sklearn.ensemble import RandomForestClassifier
import joblib

# ✅ 環境変数からAPIキーを読み込み
load_dotenv()
client = OpenAI()  # .env の OPENAI_API_KEY を自動で使用

# 🔍 GPT分析関数
def analyze_comment(text):
    prompt = f"""
    以下は社員の自由記述コメントです。
    この内容を一言で要約し、感情を「ポジティブ／ニュートラル／ネガティブ」のいずれかで分類してください。

    # コメント:
    {text}

    # 出力形式:
    要約: <要約文>
    感情: <ポジティブ or ニュートラル or ネガティブ>
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは人事部門向けのサーベイ分析AIです。"},
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content

        # 🧠 結果の抽出
        summary = ""
        sentiment = ""
        for line in content.split("\n"):
            if line.startswith("要約:"):
                summary = line.replace("要約:", "").strip()
            elif line.startswith("感情:"):
                sentiment = line.replace("感情:", "").strip()

        return summary, sentiment

    except Exception as e:
        print("⚠️ GPT分析エラー:", e)
        return "要約エラー", "感情エラー"

# 📥 ファイル読み込みと保存パス
INPUT_FILE = "survey_responses/2025-05.csv"
OUTPUT_FILE = "survey_responses/2025-05_summary.csv"

# 📊 CSV読込とGPT処理
df = pd.read_csv(INPUT_FILE)
df["要約"], df["感情"] = zip(*df["comment"].fillna("").map(analyze_comment))

# 💾 結果保存
df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ 分析完了！保存先：{OUTPUT_FILE}")

# 🧠 モデル保存（SHAP用ダミー）
model = RandomForestClassifier()
model.fit(df[["workload", "growth", "stress", "relationship"]], [0] * len(df))  # ラベルはダミー
joblib.dump(model, "model/retention_model.pkl")
print("✅ モデル保存完了：model/retention_model.pkl")
