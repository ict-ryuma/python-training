import os
print("現在の作業ディレクトリ:", os.getcwd())

import csv
from datetime import datetime

# ステップ1：ファイルが空ならヘッダー行を書く
with open("user_log.csv", mode="a+", encoding="utf-8", newline="") as file:
    file.seek(0)
    if not file.read(1):
        writer = csv.writer(file)
        writer.writerow(["名前", "年齢", "登録時刻"])

# ステップ2：情報を毎回記録
while True:
    name = input("お名前は？：")
    try:
        age = int(input("年齢は？："))
    except ValueError:
        print("⚠️ 数字で入力してください（例: 18）")
        continue

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("user_log.csv", mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, now])

    print(f"{name}さん（{age}歳）の情報を記録しました 📝")

    again = input("続けますか？（はい/いいえ）：").strip().lower()
    if again != "はい":
        print("終了します。ありがとうございました。")
        break

    import os
print("CSVのフルパス:", os.path.abspath("user_log.csv"))

