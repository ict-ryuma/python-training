import csv

# データ
people = [
    {"名前": "田中 一郎", "年齢": 25, "職業": "エンジニア"},
    {"名前": "佐藤 二郎", "年齢": 31, "職業": "営業"},
    {"名前": "鈴木 三郎", "年齢": 45, "職業": "デザイナー"},
    {"名前": "高橋 四郎", "年齢": 39, "職業": "エンジニア"}
]

# ステータス分類
for person in people:
    if person["年齢"] < 30:
        person["ステータス"] = "若手"
    elif person["年齢"] < 40:
        person["ステータス"] = "中堅"
    else:
        person["ステータス"] = "ベテラン"

# 年齢で昇順ソート
people.sort(key=lambda x: x["年齢"])

# CSVに保存
with open("people_output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["名前", "年齢", "職業", "ステータス"])
    writer.writeheader()        
    writer.writerows(people)  # ← これがないとデータが書き込まれません！

print("CSVファイルを出力しました。")  # 実行されたか目印になります

print(f"人数：{len(people)}人")
print(f"平均年齢：{average_age:.1f}歳")
for person in people:
    print(f"{customer['name']}（{customer['age']}歳）- スコア: {customer['score']}")

