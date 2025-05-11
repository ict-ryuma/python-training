# 複数の人の情報を辞書のリストとして定義
people = [
    {"name": "田中 太郎", "age": 32, "job": "エンジニア"},
    {"name": "佐藤 花子", "age": 45, "job": "デザイナー"},
    {"name": "鈴木 次郎", "age": 19, "job": "学生"}
]

# 一人ずつ表示
for person in people:
    print(f'{person["name"]} さん（{person["age"]}歳）は、{person["job"]}です。')
