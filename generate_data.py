import pandas as pd
import random

n = 100

jobs = ["営業", "Pythonエンジニア", "Goエンジニア", "デザイナー"]
genders = ["男性", "女性"]
divorces = ["あり", "なし"]

data = []

# パワハラレベルが高いと退職確率が上がるようなロジックで生成
for i in range(n):
    age = random.randint(20, 65)
    job = random.choice(jobs)
    overtime = random.randint(0, 100)
    gender = random.choice(genders)
    divorce = random.choice(divorces)
    power_harassment = random.randint(0, 10)

    # パワハラレベルが高いと True の確率を高める
    if power_harassment >= 7:
        retire = random.choices([True, False], weights=[0.95, 0.05])[0]
    elif power_harassment <= 3:
        retire = random.choices([True, False], weights=[0.05, 0.95])[0]
    else:
        retire = random.choice([True, False])

    data.append([age, job, overtime, gender, divorce, power_harassment, retire])

df = pd.DataFrame(data, columns=["年齢", "職業", "残業時間", "性別", "離婚", "パワハラレベル", "退職"])
df.to_csv("ml_sample.csv", index=False)
