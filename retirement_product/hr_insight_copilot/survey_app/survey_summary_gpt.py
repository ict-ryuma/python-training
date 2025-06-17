import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI

# ✅ .envからAPIキーを読み込み
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 📥 サマリーファイルを読み込み
CSV_FILE = "survey_responses/2025-05_summary.csv"
df = pd.read_csv(CSV_FILE)

# 🎯 感情集計
n_total = len(df)
n_positive = (df["感情"] == "ポジティブ").sum()
n_neutral = (df["感情"] == "ニュートラル").sum()
n_negative = (df["感情"] == "ネガティブ").sum()

# 🧠 コメント要約統合
all_summaries = "\n".join(df["要約"].dropna().tolist())

# 📤 プロンプト
prompt = f"""
あなたは人事部門のレポート支援AIです。
以下は従業員のコメント要約と感情集計です。

- 総コメント数: {n_total}
- ポジティブ: {n_positive}
- ニュートラル: {n_neutral}
- ネガティブ: {n_negative}

コメント要約一覧:
{all_summaries}

この情報をもとに、次の3点を出力してください：
1. 組織全体の傾向を一言で要約
2. 特に注意すべき傾向や兆候（離職リスク）
3. 人事への推奨アクション（日本語で丁寧に）

出力フォーマット：
---
🔍 組織傾向：...
⚠️ 注意ポイント：...
💡 推奨アクション：...
---
"""

# 🔁 GPT 実行（v1対応）
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたは人事部向けの要約レポート生成AIです。"},
        {"role": "user", "content": prompt}
    ]
)

# ✅ 出力
print("\n✅ GPT組織レポート:\n")
print(response.choices[0].message.content)
