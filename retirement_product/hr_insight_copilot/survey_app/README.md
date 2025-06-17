hr_insight_copilot/
├── survey_app/                      ← サーベイ入力・保存・表示用
│   ├── survey_app.py                ← メインアプリ
│   ├── survey_questions.py         ← 質問定義（リスト or Dict）
│   ├── survey_storage.py           ← 回答の保存・読み込み
│   └── survey_responses/           ← 回答CSVが日付単位で保存されるフォルダ
│       └── 2025-05.csv             ← 月ごとの回答記録
