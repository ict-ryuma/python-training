import csv

def filter_engineers_over_30(people):
    result = []
    for person in people:
        if "エンジニア" in person["職業"] and person["年齢"] >= 30:  # ここに「職業」と「年齢」の条件
            result.append(person)
    return result

# 人物データ
people = [
    {"名前": "田中 一郎", "年齢": 25, "職業": "Pythonエンジニア"},
    {"名前": "佐藤 二郎", "年齢": 31, "職業": "営業"},
    {"名前": "鈴木 三郎", "年齢": 42, "職業": "PHPエンジニア"},
    {"名前": "中村 四郎", "年齢": 35, "職業": "Javaデザイナー"}
]

# 関数で抽出
engineer_list = filter_engineers_over_30(people)

# CSVに書き出し
with open("engineers_over_30.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["名前", "年齢", "職業"])
    writer.writeheader()
    writer.writerows(engineer_list)

print("✅ エンジニア一覧をCSVに出力しました！")
