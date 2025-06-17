# 💼 退職リスク診断アプリ

このアプリは、ユーザーの勤務状況やパーソナルな属性を元に、退職リスクをAIで診断し、対策を提示するWebアプリです。  
また、チャットUIを通じて気軽に相談形式で診断を受けることもできます。

---

## 🚀 特徴

- Streamlit製の軽量Webアプリ
- 入力フォーム or チャットUIの2通りの診断方法
- パワハラレベルなどのパラメータを調整し、最適な環境条件を自動提案
- 過去の学習データに基づいた退職リスクの予測（モデルは`joblib`で読み込み）
- 将来的にはSHAPや分析ダッシュボード、サーベイ連携にも対応可能

---

## 🧰 使用技術

- Python 3.10+
- Streamlit
- Scikit-learn（退職予測モデル）
- Pandas / Joblib
- dotenv（OpenAIなど外部キー管理）

---

## 📁 フォルダ構成

retirement_product/
├── app.py # メインアプリ（フォーム＋チャットUI）
├── model.pkl # 学習済み予測モデル
├── le_job.pkl # 職業のLabelEncoder
├── le_gender.pkl # 性別のLabelEncoder
├── le_divorce.pkl # 離婚経験のLabelEncoder
├── .env # OPENAI_API_KEYなどの環境変数
└── README.md # このファイル


---

## 📝 実行方法

1. 仮想環境に入る（例：`venv`）
    ```bash
    source venv/bin/activate
    ```

2. 必要なライブラリをインストール
    ```bash
    pip install -r requirements.txt
    ```

3. `.env` ファイルにAPIキーを記述
    ```
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxx
    ```

4. アプリを起動
    ```bash
    streamlit run app.py
    ```

5. ブラウザで `http://localhost:8501` を開く

---

## ✅ 現在のUI構成

- **フォーム入力セクション**：年齢・職業・残業時間・性別・離婚経験・パワハラレベルなどを入力
- **リスク診断結果**：退職リスク確率とパワハラ耐久シミュレーション
- **チャット形式セクション**：自然文から自動的に状況を抽出し、同様に診断
- **今後追加予定**：
    - SHAP可視化による要因分析
    - GPT相談へのフィードバックロギング
    - サーベイ/Geppo連携（組織改善向け）

---

## 👨‍🔧 開発者メモ

このアプリは、実務応用や副業ポートフォリオとしても展開可能です。  
開発目的やカスタマイズ方針を `README` に都度追記してください。

---

## 📮 お問い合わせ

本アプリに関する質問・改善提案は開発者までご連絡ください。

