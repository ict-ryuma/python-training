import csv

# エンジニアを抽出する関数
def filter_engineers(people):
    result = []
    for person in people:
        if "エンジニア" in person["職業"]:
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
engineer_list = filter_engineers(people)

# CSVに書き出し
with open("engineers_output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["名前", "年齢", "職業"])
    writer.writeheader()
    writer.writerows(engineer_list)

print("✅ エンジニア一覧をCSVに出力しました！")
