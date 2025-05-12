people = [
    {"名前": "田中 一郎", "年齢": 25, "職業": "エンジニア"},
    {"名前": "佐藤 二郎", "年齢": 31, "職業": "営業"},
]
for person in people:
    if person["年齢"] < 30:
        person["ステータス"] = "若手"
    elif person["年齢"] < 40:
        person["ステータス"] = "中堅"
    else:
        person["ステータス"] = "ベテラン"

print(f"{person['名前']}（{person['年齢']}歳／{person['職業']}）")