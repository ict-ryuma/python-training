# ユーザー情報のリスト（辞書で管理）
customers = [
    {"name": "田中 花子", "age": 18},
    {"name": "山田 太郎", "age": 45},
    {"name": "星 竜馬", "age": 66},
    {"name": "雨野 一郎", "age": 12}
]

# 各ユーザーの年齢に応じたカテゴリを表示
for person in customers:
    name = person["name"]
    age = person["age"]
    
    if age >= 65:
        category = "シニア"
    elif age >= 20:
        category = "成人"
    else:
        category = "未成年"

    print(f"{name} さん（{age}歳）は {category} です。")
