def filter_engineers(people):
    result = []
    for person in people:
        if "エンジニア" in person["職業"] :
            result.append(person)
    return result

people = [
    {"名前": "田中 一郎", "年齢": 25, "職業": "Pythonエンジニア"},
    {"名前": "佐藤 二郎", "年齢": 31, "職業": "営業"},
    {"名前": "高橋 三郎", "年齢": 42, "職業": "PHPエンジニア"},
    {"名前": "中村 四郎", "年齢": 35, "職業": "Javaデザイナー"}
]

# 関数で抽出
jobengineerlist = filter_engineers(people)

# 結果を表示
for person in jobengineerlist:
    print(f"{person['名前']} さん ({person['年齢']}歳) エンジニアスキル: {person['職業']}")
