people = [
    {"名前": "田中 一郎", "年齢": 25, "職業": "エンジニア"},
    {"名前": "佐藤 二郎", "年齢": 31, "職業": "営業"},
    {"名前": "鈴木 三郎", "年齢": 45, "職業": "デザイナー"},
    {"名前": "高橋 四郎", "年齢": 39, "職業": "エンジニア"}
]

# ステータス分類を追加
for person in people:
    if person["年齢"] < 30:
        person["ステータス"] = "若手"
    elif person["年齢"] < 40:
        person["ステータス"] = "中堅"
    else:
        person["ステータス"] = "ベテラン"

# 年齢で昇順にソート
people.sort(key=lambda x: x["年齢"])

# 整形して出力
for person in people:
    print(f"{person['名前']}（{person['年齢']}歳／{person['職業']}／{person['ステータス']}）")
