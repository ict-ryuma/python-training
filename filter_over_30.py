def filter_over_30(people):
    result = []
    for person in people:
        if person["年齢"] >= 30:
            result.append(person)
    return result

# データ
people = [
    {"名前": "田中 一郎", "年齢": 25},
    {"名前": "佐藤 二郎", "年齢": 31},
    {"名前": "高橋 三郎", "年齢": 42}
]

# 関数で抽出
over_30_list = filter_over_30(people)

# 結果を表示
for person in over_30_list:
    print(f"{person['名前']} さん（{person['年齢']}歳）")
